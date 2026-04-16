import socket

class UDPScanner:
    def __init__(self, timeout=2):
        self.timeout = timeout

    def scan_port(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(self.timeout)
            sock.sendto(b'', (ip, port))

            try:
                data, _ = sock.recvfrom(1024)
                return {"port": port, "state": "open", "protocol": "UDP"}
            except socket.timeout:
                # No response = open|filtered (common for UDP)
                return {"port": port, "state": "open|filtered", "protocol": "UDP"}

        except Exception as e:
            return {"port": port, "state": "closed", "protocol": "UDP"}
        finally:
            sock.close()

    def scan(self, ip, ports):
        results = []
        for port in ports:
            result = self.scan_port(ip, port)
            results.append(result)
        return results