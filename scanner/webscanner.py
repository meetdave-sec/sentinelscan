import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-XSS-Protection",
    "Strict-Transport-Security"
]


def scan_web(target):
    print(f"\n[+] Starting web scan for: {target}")
    
    url = f"http://{target}"

    try:
        response = requests.get(url, timeout=5)

        print(f"[+] HTTP response code: {response.status_code}")

        headers = response.headers

        https_url = f"https://{target}"
        try:
            https_response = requests.get(https_url, timeout=5)
            print("[+] HTTPS is enabled")
        except:
            print("[!] HTTPS not available (possible misconfiguration)")
       
        print("\n[+] Security Header Analysis:")

        for header in SECURITY_HEADERS:
            if header not in headers:
                print(f"[WARNING] Missing header: {header}")
            else:
                print(f"[OK] {header} present")

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Web scan failed: {e}")
