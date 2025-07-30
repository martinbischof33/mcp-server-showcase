# MCP Appointment Scheduler Backend

This repository contains a **FastMCP** server that wraps the CalDoc REST API and exposes it as a set of MCP tools.  It powers conversational agents that can

* look-up callers by phone number,
* list practice locations and appointment types,
* show the next free slots, and
* book, move, or cancel appointments.

---

## Requirements

* Python **3.12** or later
* [`uv`](https://github.com/astral-sh/uv) 
> or grab a pre-built binary from the [releases page](https://github.com/astral-sh/uv/releases).

---

## Quickstart (TL;DR)

```bash
# 1. clone the repo & enter it
$ git clone <this-repo-url> mcp-backend
$ cd mcp-backend

# 2. create a virtual environment and install the deps (takes ~2-3 s with uv)
$ uv venv          # creates .venv/ and activates it automatically
$ source .venv/bin/activate  # only necessary if your shell did not activate it
$ uv pip install -e .        # install the project in *editable* mode

# 3. copy / adjust environment variables
$ cp .env .env.local         # change CALDOC_API_URL if needed

# install the mcp server to claude config
$ mcp install server.py

# 4. run the server (stdio transport ‑– best for local dev)
$ mcp run server.py
```


