import argparse
import time
from utils.ip_utils import resolve_hostname, is_valid_ip, expand_ip_range, parse_port_range
from utils.logger import Logger
from utils.exporter import Exporter
from scanner.tcp_scanner import TCPScanner

def main():
    parser = argparse.ArgumentParser(
        description="Advanced Port Scanner - Educational Tool",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("target", help="IP address, hostname, or range (e.g. 192.168.1.1 or 192.168.1.0/24)")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range (e.g. 1-1000, 80,443,22, 80)")
    parser.add_argument("-t", "--threads", type=int, default=200, help="Number of threads (default: 200)")
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout in seconds (default: 1.0)")
    parser.add_argument("--no-banner", action="store_true", help="Disable banner grabbing")
    parser.add_argument("--export", choices=["json", "csv", "both"], help="Export results")

    args = parser.parse_args()

    print("\n" + "="*60)
    print("         FIRST PORT SCANNER")
    print("="*60 + "\n")

    # Resolve hostname to IP
    ip = resolve_hostname(args.target) if not is_valid_ip(args.target) else args.target
    if not ip:
        Logger.error(f"Could not resolve host: {args.target}")
        return

    Logger.info(f"Target  : {args.target} ({ip})")
    Logger.info(f"Ports   : {args.ports}")
    Logger.info(f"Threads : {args.threads}")
    Logger.info(f"Timeout : {args.timeout}s\n")

    # Parse ports
    port_input = parse_port_range(args.ports)
    if isinstance(port_input, list):
        port_range = (min(port_input), max(port_input))
    else:
        port_range = port_input

    # Start scan
    start_time = time.time()
    Logger.info("Starting TCP scan...")

    scanner = TCPScanner(
        timeout=args.timeout,
        threads=args.threads,
        grab_banners=not args.no_banner
    )

    results = scanner.scan(ip, port_range)
    elapsed = round(time.time() - start_time, 2)

    # Display results
    print()
    if results:
        Logger.success(f"Found {len(results)} open port(s):\n")
        for r in results:
            Logger.port_open(r['port'], r['service'], r['banner'])
    else:
        Logger.warning("No open ports found in the given range.")

    print()
    Logger.info(f"Scan completed in {elapsed} seconds")

    # Export if requested
    if args.export and results:
        exporter = Exporter()
        if args.export in ["json", "both"]:
            path = exporter.export_json(ip, results)
            Logger.success(f"JSON saved: {path}")
        if args.export in ["csv", "both"]:
            path = exporter.export_csv(ip, results)
            Logger.success(f"CSV saved: {path}")

if __name__ == "__main__":
    main()