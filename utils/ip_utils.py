import socket
import ipaddress

def resolve_hostname(host):
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return None

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def expand_ip_range(ip_range):
    """
    Accepts:
    - Single IP: 192.168.1.1
    - CIDR: 192.168.1.0/24
    - Range: 192.168.1.1-10
    Returns list of IP strings
    """
    if '/' in ip_range:
        network = ipaddress.ip_network(ip_range, strict=False)
        return [str(ip) for ip in network.hosts()]
    elif '-' in ip_range:
        base, end = ip_range.rsplit('.', 1)[0], ip_range.split('-')
        start_ip = ip_range.split('-')[0]
        end_last = int(ip_range.split('-')[1])
        start_last = int(start_ip.split('.')[-1])
        base_ip = '.'.join(start_ip.split('.')[:-1])
        return [f"{base_ip}.{i}" for i in range(start_last, end_last + 1)]
    else:
        return [ip_range]

def parse_port_range(port_input):
    """
    Accepts:
    - Single port: 80
    - Range: 1-1000
    - List: 22,80,443
    Returns (start, end) tuple or list of ports
    """
    if '-' in port_input:
        start, end = port_input.split('-')
        return (int(start), int(end))
    elif ',' in port_input:
        return [int(p) for p in port_input.split(',')]
    else:
        port = int(port_input)
        return (port, port)