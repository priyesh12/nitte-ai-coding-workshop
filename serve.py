#!/usr/bin/env python3
"""Hand the workshop out from your own laptop. No GitHub, no USB, no internet.

    python3 serve.py

Builds a student ZIP (answers stripped out), starts a web server, and prints
the address to write on the board. Students open it in a browser and download.

Ctrl-C to stop.
"""
from __future__ import annotations

import http.server
import pathlib
import shutil
import socket
import socketserver
import tempfile
import zipfile

PORT = 8000

# Student-facing only. instructor/ is deliberately excluded.
INCLUDE_DIRS = ["bugs", "placement_tracker", "handouts", "harnesses"]
INCLUDE_FILES = ["check_setup.py", "run_tests.py", "README.md", "CURRICULUM.md"]
ZIP_NAME = "workshop.zip"


def lan_ip() -> str:
    """Best guess at this machine's address on the classroom network."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))  # no packets sent; just picks the interface
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


def build_zip(root: pathlib.Path, out: pathlib.Path) -> int:
    n = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for name in INCLUDE_FILES:
            f = root / name
            if f.is_file():
                z.write(f, f"workshop/{name}")
                n += 1
        for d in INCLUDE_DIRS:
            for f in sorted((root / d).rglob("*")):
                if f.is_file() and "__pycache__" not in f.parts:
                    z.write(f, f"workshop/{f.relative_to(root)}")
                    n += 1
    return n


INDEX = """<!doctype html><meta charset=utf-8>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>Workshop download</title>
<style>
 body{{font:16px/1.6 system-ui,sans-serif;max-width:34rem;margin:0 auto;
      padding:2rem 1rem;color:#111;background:#fafafa}}
 a.dl{{display:block;background:#0b5;color:#fff;text-align:center;padding:1rem;
      border-radius:.5rem;font-size:1.25rem;font-weight:700;text-decoration:none;
      margin:1.5rem 0}}
 code{{background:#eee;padding:.15rem .4rem;border-radius:.25rem}}
 pre{{background:#eee;padding:.75rem;border-radius:.4rem;overflow-x:auto}}
 ol{{padding-left:1.2rem}} li{{margin:.6rem 0}}
</style>
<h1>AI Coding &amp; Debugging Workshop</h1>
<a class=dl href="/{zip}">Download workshop.zip</a>
<ol>
 <li>Download and <b>unzip</b> it.</li>
 <li>Open a terminal in the unzipped <code>workshop</code> folder.</li>
 <li>Run:<pre>python3 check_setup.py</pre></li>
 <li>Then:<pre>python3 run_tests.py bugs</pre></li>
</ol>
<p>You should see <b>18 passing, 16 failing</b>.
<b>The failures are the workshop.</b></p>
<p>No Python? Windows: install <b>Python 3.12</b> from the Microsoft Store
(no admin rights needed). Mac/Linux: you already have it.</p>
"""


def main() -> None:
    root = pathlib.Path(__file__).parent.resolve()
    serve_dir = pathlib.Path(tempfile.mkdtemp(prefix="workshop-serve-"))
    count = build_zip(root, serve_dir / ZIP_NAME)
    (serve_dir / "index.html").write_text(INDEX.format(zip=ZIP_NAME))

    size = (serve_dir / ZIP_NAME).stat().st_size / 1024
    ip = lan_ip()
    bar = "=" * 52

    print(f"\n{bar}")
    print(f"  Packed {count} files  ({size:.0f} KB)  - answers excluded")
    print(bar)
    print("\n  WRITE THIS ON THE BOARD:\n")
    print(f"      http://{ip}:{PORT}\n")
    print(f"{bar}")
    print("  Students: type that into any browser, download, unzip.")
    print("  Works with NO internet - just the same wifi as this laptop.")
    print("  Ctrl-C when everyone has it.")
    print(f"{bar}\n")

    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=str(serve_dir), **kw)

        def log_message(self, fmt, *args):
            if "workshop.zip" in (args[0] if args else ""):
                print(f"  downloaded by {self.client_address[0]}")

    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Stopped.\n")
    finally:
        shutil.rmtree(serve_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
