#!/usr/bin/env python3
"""
scanner_demo.py

This file demonstrates the core philosophy behind the scanner:
report only observable and meaningful security signals,
not theoretical or speculative issues.

This is NOT a full scanner.
It is a minimal, readable demo intended to explain behavior.
"""

import sys
import requests


def scan(url: str) -> None:
    """
    Perform a minimal, execution-oriented security check.

    The purpose of this function is to demonstrate how
    security signals are collected, not to exhaustively scan a target.
    """
    print(f"[+] Starting demo scan for: {url}")

    try:
        response = requests.get(url, timeout=10)
    except Exception as exc:
        print(f"[-] Request failed: {exc}")
        return

    headers = response.headers

    # --- Security Header Check ---
    # We only report what we can directly observe.
    if "Content-Security-Policy" not in headers:
        print("[!] Missing Content-Security-Policy header")
    else:
        print("[✓] Content-Security-Policy header present")

    # --- Cookie Observation ---
    # This demo intentionally avoids deep cookie flag analysis.
    cookies = response.cookies
    if cookies:
        print("[!] Cookies detected (demo-level observation)")
    else:
        print("[✓] No cookies detected")

    print("[✓] Demo scan completed")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner_demo.py https://example.com")
        sys.exit(1)

    scan(sys.argv[1])
