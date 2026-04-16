# 🔍 Python Port Scanner

An advanced multithreaded **TCP port scanner** built in Python with service detection and banner grabbing. Designed for **network analysis and educational purposes**.

---

## 🚀 Features

* ⚡ Multithreaded TCP scanning (fast performance)
* 🔎 Service detection using port mapping
* 🏷 Banner grabbing for deeper insights
* 🌐 Supports IP, hostname, and ranges
* 📊 Export results to JSON and CSV
* 🎯 Custom port ranges and thread control
* 🧩 Modular and clean code structure

---

## 📁 Project Structure

```
port-scanner/
│
├── scanner/              # Core scanning logic
│   ├── tcp_scanner.py
│   ├── udp_scanner.py
│   ├── banner_grabber.py
│   └── service_detector.py
│
├── utils/                # Helper utilities
│   ├── ip_utils.py
│   ├── exporter.py
│   └── logger.py
│
├── data/                 # Service-port mappings
│   └── service_ports.json
│
├── results/              # Scan outputs (ignored in git)
│
├── main.py               # Entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/het2025/Port_Scanner.git
cd port-scanner
pip install -r requirements.txt
```

---

## 🧪 Usage

### 🔹 Basic Scan

```bash
python main.py 192.168.1.1
```

### 🔹 Scan Specific Port Range

```bash
python main.py 192.168.1.1 -p 1-10000
```

### 🔹 Scan Specific Ports

```bash
python main.py 192.168.1.1 -p 22,80,443
```

### 🔹 Increase Speed (Threads)

```bash
python main.py 192.168.1.1 -t 500
```

### 🔹 Disable Banner Grabbing

```bash
python main.py 192.168.1.1 --no-banner
```

### 🔹 Export Results

```bash
python main.py 192.168.1.1 --export json
```

---

## 📌 Example Output

```
[+] Found 2 open port(s):

  [OPEN]  Port 22     SSH
  [OPEN]  Port 80     HTTP
```

---

## ⚠️ Disclaimer

This tool is developed for **educational purposes only**.

* Do NOT scan systems without permission
* Unauthorized scanning may be illegal
* The developer is not responsible for misuse

---

## 🧠 Future Improvements

* SYN scan (stealth scanning)
* OS fingerprinting
* Real-time progress bar
* Service detection via banners
* GUI interface

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit pull requests.

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!

---
