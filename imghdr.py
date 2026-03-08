"""A lightweight replacement for the Python standard library `imghdr` module.

This file is included because some Python environments (e.g., trimmed/embedded
builds used by some hosting providers) may omit the stdlib `imghdr` module.
Streamlit expects it for image format detection.

This implementation is intentionally small and supports the subset of image
formats commonly used by Streamlit.
"""

from __future__ import annotations

from pathlib import Path
from typing import BinaryIO, Optional, Union


def _read_bytes(data: Union[str, bytes, Path, BinaryIO], n: int = 32) -> bytes:
    if isinstance(data, (bytes, bytearray)):
        return bytes(data[:n])

    if isinstance(data, str):
        with open(data, "rb") as f:
            return f.read(n)

    if isinstance(data, Path):
        with data.open("rb") as f:
            return f.read(n)

    # Assume a file-like object
    pos = None
    try:
        pos = data.tell()
    except Exception:
        pass

    head = data.read(n)
    if pos is not None:
        try:
            data.seek(pos)
        except Exception:
            pass
    return head


def what(file: Union[str, Path, BinaryIO, bytes], h: Optional[bytes] = None) -> Optional[str]:
    """Determine the type of image contained in a file or byte stream."""
    if h is None:
        h = _read_bytes(file)
    if not h:
        return None

    # JPEG
    if h.startswith(b"\xff\xd8\xff"):
        return "jpeg"

    # PNG
    if h.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"

    # GIF
    if h.startswith(b"GIF87a") or h.startswith(b"GIF89a"):
        return "gif"

    # TIFF
    if h.startswith(b"II*\x00") or h.startswith(b"MM\x00*"):
        return "tiff"

    # BMP
    if h.startswith(b"BM"):
        return "bmp"

    # WebP
    if h.startswith(b"RIFF") and b"WEBP" in h[8:12]:
        return "webp"

    # ICO
    if h.startswith(b"\x00\x00\x01\x00"):
        return "ico"

    # JPEG 2000
    if h.startswith(b"\x00\x00\x00\x0c") and b"jP  " in h[4:12]:
        return "jp2"

    return None


# Expose a minimal subset of the standard imghdr API.
__all__ = ["what"]
