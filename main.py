from scanner.port_scanner import scan_ports
from scanner.webscanner import scan_web
from reports.report_generator import save_report

def main():
    print("\n==============================")
    print("     SENTINELSCAN v1.0")
    print("==============================\n")

    target = input("Enter target IP or domain: ").strip()

    if not target:
        print("[!] Invalid target. Exiting.")
        return

    open_ports = scan_ports(target)
    web_findings = scan_web(target)

    save_report(target, open_ports, web_findings)

    print("\n==============================")
    print("SCAN COMPLETE")
    print("==============================")


if __name__ == "__main__":
    main()             