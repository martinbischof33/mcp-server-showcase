"""Typed models for CalDoc /voice/locations/ endpoint.

These models mirror the JSON schema documented in `apispec.json` so that:
1.  Runtime validation is performed when data is parsed from the HTTP response.
2.  MCP can automatically generate correct function metadata & JSON schemas.
3.  Developers get rich autocompletion and static-type checking.

Only the subset of fields present in the spec is modelled here – extend if the
backend returns additional keys.
"""

from __future__ import annotations

from pydantic import BaseModel


class AddResponse(BaseModel):
    """Response schema for diverse request API."""
    result: int