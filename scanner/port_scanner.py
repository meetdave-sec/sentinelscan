import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

def scan_ports(target, timeout=1):
    print(f"\n[+] Scanning target: {target}")

    open_ports = []

    for port, service in COMMON_PORTS.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        try:
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] {port} ({service})")
                open_ports.append((port, service))

        except Exception as e:
            print(f"[ERROR] {port}: {e}")    

        finally:
            sock.close()    

    return open_ports        