#!/usr/bin/env python3
"""Verifica o site em docs/: todo link e asset interno aponta para um arquivo que existe.

    python3 scripts/check-site.py
"""

import os
import re
import sys
from urllib.parse import unquote, urldefrag

DOCS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
ATTR = re.compile(r'(?:href|src)="([^"]+)"')
BASE = "/oh-my-harness/"
EXTERNAL = ("http://", "https://", "mailto:", "data:", "tel:", "#")


def broken_links(page):
    with open(os.path.join(DOCS, page), encoding="utf-8") as f:
        html = f.read()
    for ref in ATTR.findall(html):
        if ref.startswith(EXTERNAL):
            continue
        target = unquote(urldefrag(ref)[0])
        if target.startswith(BASE):  # o 404.html usa caminho absoluto do subcaminho do Pages
            target = target[len(BASE):] or "index.html"
        if target and not os.path.exists(os.path.join(DOCS, target)):
            yield ref


def main():
    pages = sorted(p for p in os.listdir(DOCS) if p.endswith(".html"))
    problems = [(p, ref) for p in pages for ref in broken_links(p)]
    for page, ref in problems:
        print(f"X {page}: link quebrado -> {ref}")
    print(f"{len(pages)} páginas · {len(problems)} problemas")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
