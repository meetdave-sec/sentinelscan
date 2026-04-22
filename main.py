import uuid
from datetime import datetime

from scanner.port_scanner import scan_ports
from scanner.webscanner import scan_web
from reports.html_report import generate_html_report


def main():
    print("\n==============================")
    print("     SENTINELSCAN v1.0")
    print("==============================\n")

    target = input("Enter target IP or domain: ").strip()

    if not target:
        print("[!] Invalid target. Exiting.")
        return
 
    scan_id = str(uuid.uuid4())[:8]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n[+] Scan ID: {scan_id}")
    print(f"[+] Timestamp: {timestamp}")

    open_ports = scan_ports(target)
    web_findings = scan_web(target)
   
    generate_html_report(target, open_ports, web_findings)

    print("\n==============================")
    print("SCAN COMPLETE")
    print("==============================")


if __name__ == "__main__":
    main()