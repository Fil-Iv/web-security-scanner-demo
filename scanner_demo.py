#!/usr/bin/env python3
import sys
import requests

def scan(url):
    print(f"[+] Scanning {url}")
    try:
        r = requests.get(url, timeout=10)
    except Exception as e:
        print(f"[-] Request failed: {e}")
        return

    headers = r.headers

    if "Content-Security-Policy" not in headers:
        print("[!] Missing Content-Security-Policy header")

    cookies = r.cookies
    if cookies:
        print("[!] Cookies detected (demo check)")
    else:
        print("[✓] No cookies detected")

    print("[✓] Demo scan finished")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner_demo.py https://example.com")
        sys.exit(1)
    scan(sys.argv[1])
