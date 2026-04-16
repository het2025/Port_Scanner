import json
import os

class ServiceDetector:
    def __init__(self):
        data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'service_ports.json')
        with open(data_path, 'r') as f:
            self.services = json.load(f)

    def get_service(self, port):
        return self.services.get(str(port), "Unknown")