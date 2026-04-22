import requests
from utils.helpers import print_result

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
        print_result("INFO", "Checking HTTPS availability...")
        try:
            requests.get(https_url, timeout=5)
            print_result("OK", "HTTPS is enabled")
        except:
            print_result("HIGH", "HTTPS is NOT enabled (security risk)")
       
        print("\n[+] Security Header Analysis:")

        for header in SECURITY_HEADERS:
            if header not in headers:
                print_result("MEDIUM", f"Missing security header: {header}")
            else:
                print_result("OK", f"{header} is present")

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Web scan failed: {e}")
        

    findings = []

    security_headers = {
    "Content-Security-Policy": "Prevents XSS and injection attacks",
    "X-Frame-Options": "Prevents clickjacking attacks",
    "X-XSS-Protection": "Legacy XSS protection",
    "Strict-Transport-Security": "Enforces HTTPS usage"
    }

    for header, description in security_headers.items():
        if header not in headers:
            findings.append({
                "issue": f"Missing {header}",
                "severity": "MEDIUM",
                "description": description
            })    

    return findings
