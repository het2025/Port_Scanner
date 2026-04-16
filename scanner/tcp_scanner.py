import socket
import concurrent.futures
import threading
from scanner.banner_grabber import BannerGrabber
from scanner.service_detector import ServiceDetector

class TCPScanner:
    def __init__(self, timeout=1, threads=200, grab_banners=True):
        self.timeout = timeout
        self.threads = threads
        self.grab_banners = grab_banners
        self.banner_grabber = BannerGrabber(timeout=2)
        self.service_detector = ServiceDetector()
        self.results = []
        self.lock = threading.Lock()

    def scan_port(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((ip, port))  # returns 0 if open
            sock.close()

            if result == 0:
                service = self.service_detector.get_service(port)
                banner = None
                if self.grab_banners:
                    banner = self.banner_grabber.grab(ip, port)

                port_data = {
                    "port": port,
                    "state": "open",
                    "service": service,
                    "banner": banner
                }

                with self.lock:
                    self.results.append(port_data)

                return port_data
            return None

        except Exception:
            return None

    def scan(self, ip, port_range):
        self.results = []
        start_port, end_port = port_range

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = {
                executor.submit(self.scan_port, ip, port): port
                for port in range(start_port, end_port + 1)
            }
            concurrent.futures.wait(futures)

        # Sort results by port number
        self.results.sort(key=lambda x: x['port'])
        return self.results