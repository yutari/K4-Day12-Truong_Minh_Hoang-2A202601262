"""Structured JSON logging for cloud log collectors."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from typing import Any


def utc_now_iso() -> str:
    """Return the current UTC time in ISO-8601 format."""
    return datetime.now(timezone.utc).isoformat()


def emit(event: str, severity: str = "INFO", **fields: Any) -> str:
    """Write one JSON log record to stdout and return its serialized form."""
    record = {
        "event": event,
        "severity": severity.upper(),
        "ts": utc_now_iso(),
        **fields,
    }
    line = json.dumps(record, ensure_ascii=False)
    print(line, file=sys.stdout, flush=True)
    return line
