import json
import csv
import os
from datetime import datetime

class Exporter:
    def __init__(self, output_dir="results"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def _generate_filename(self, ip, extension):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_ip = ip.replace('.', '_')
        return os.path.join(self.output_dir, f"scan_{safe_ip}_{timestamp}.{extension}")

    def export_json(self, ip, results):
        filename = self._generate_filename(ip, "json")
        data = {
            "target": ip,
            "scan_time": datetime.now().isoformat(),
            "open_ports": len(results),
            "results": results
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        return filename

    def export_csv(self, ip, results):
        filename = self._generate_filename(ip, "csv")
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["port", "state", "service", "banner"])
            writer.writeheader()
            writer.writerows(results)
        return filename