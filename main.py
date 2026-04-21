from scanner.port_scanner import scan_ports

def main():
    print("\n==============================")
    print("     SENTINELSCAN v1.0")
    print("==============================\n")

    target = input("Enter target IP or domain: ").strip()

    if not target:
        print("[!] Invalid target. Exiting")
        return
    
    results = scan_ports(target)

    print("\n==============================")
    print("SCAN COMPLETE")
    print("==============================")

    if results: 
        print("\nOpen ports found")
        for port, service in results:
            print(f" - {port} ({service})")

    else:
        print("No common open ports detected.") 


if __name__ == "__main__":
    main()             