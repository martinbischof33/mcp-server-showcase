# MCP Server Deployment Guide

This guide explains how to deploy your MCP Appointment Scheduler server on specific IP addresses and ports.

## Deployment Options

Your MCP server now supports multiple deployment methods:

### 1. Quick HTTP Deployment (Recommended for Production)

```bash
# Deploy on default settings (0.0.0.0:8000)
python deploy.py

# Deploy on specific IP and port
python deploy.py --host 192.168.1.100 --port 9000

# Deploy on localhost only
python deploy.py --host 127.0.0.1 --port 8080
```

### 2. Environment Variable Configuration

Create or modify `.env.deployment`:
```env
MCP_HOST=192.168.1.100
MCP_PORT=9000
MCP_TRANSPORT=streamable-http
```

Then run:
```bash
python deploy.py
```

### 3. Direct Python Execution

Set environment variables and run directly:
```bash
export MCP_HOST=0.0.0.0
export MCP_PORT=8000
export MCP_TRANSPORT=streamable-http
python server.py
```

### 4. Development Mode

For local development (stdio transport):
```bash
python deploy.py --dev
```

## Deployment Configurations

### Production Deployment
```bash
# On all network interfaces, port 8000
python deploy.py --host 0.0.0.0 --port 8000

# On specific server IP
python deploy.py --host 192.168.1.100 --port 9000
```

### Localhost Only
```bash
# Only accessible from the same machine
python deploy.py --host 127.0.0.1 --port 8080
```

### Custom Environment File
```bash
# Use a custom environment configuration
python deploy.py --env-file .env.production
```

## Server Features

- **Stateless HTTP Mode**: Enabled by default for better scalability
- **Streamable HTTP Transport**: Modern transport method for production
- **Environment Configuration**: Flexible configuration via environment variables
- **Graceful Shutdown**: Supports Ctrl+C for clean shutdown

## Client Connection

Once deployed, clients can connect to your MCP server using:

```
http://your-ip-address:port
```

For example, if deployed on `192.168.1.100:8000`:
```
http://192.168.1.100:8000
```

## Security Considerations

- **Firewall**: Ensure your firewall allows traffic on the chosen port
- **Network Access**: Use `127.0.0.1` for localhost-only access
- **HTTPS**: Consider using a reverse proxy (nginx, Apache) for HTTPS in production
- **Authentication**: The current server doesn't include authentication - add as needed

## Monitoring and Logs

The server outputs startup information including:
- Host and port configuration
- Transport method
- API base URL

Monitor the console output for any errors or connection issues.

## Production Deployment with systemd (Linux)

Create a systemd service file:

```ini
[Unit]
Description=MCP Appointment Scheduler
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/path/to/mcp-backend
Environment=MCP_HOST=0.0.0.0
Environment=MCP_PORT=8000
Environment=MCP_TRANSPORT=streamable-http
ExecStart=/path/to/python server.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip install -e .

EXPOSE 8000

ENV MCP_HOST=0.0.0.0
ENV MCP_PORT=8000
ENV MCP_TRANSPORT=streamable-http

CMD ["python", "server.py"]
```

Build and run:
```bash
docker build -t mcp-appointment-scheduler .
docker run -p 8000:8000 mcp-appointment-scheduler
```

## Troubleshooting

### Port Already in Use
```bash
# Check what's using the port
lsof -i :8000

# Use a different port
python deploy.py --port 8001
```

### Permission Denied (ports < 1024)
```bash
# Use a port > 1024 or run with sudo (not recommended)
python deploy.py --port 8080
```

### Network Interface Issues
```bash
# Check available interfaces
ip addr show

# Use specific interface IP
python deploy.py --host 192.168.1.100
``` 