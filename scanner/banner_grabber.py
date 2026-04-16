import socket

class BannerGrabber:
    def __init__(self, timeout=2):
        self.timeout = timeout

    def grab(self, ip, port):
        try:
            sock = socket.socket()
            sock.settimeout(self.timeout)
            sock.connect((ip, port))
            
            # Some services need you to send something first
            sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
            
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            sock.close()
            return banner if banner else None
        except Exception:
            return None