from colorama import Fore, Style, init
init(autoreset=True)

class Logger:
    @staticmethod
    def success(msg):
        print(f"{Fore.GREEN}[+] {msg}{Style.RESET_ALL}")

    @staticmethod
    def error(msg):
        print(f"{Fore.RED}[-] {msg}{Style.RESET_ALL}")

    @staticmethod
    def info(msg):
        print(f"{Fore.CYAN}[*] {msg}{Style.RESET_ALL}")

    @staticmethod
    def warning(msg):
        print(f"{Fore.YELLOW}[!] {msg}{Style.RESET_ALL}")

    @staticmethod
    def port_open(port, service, banner=None):
        banner_text = f" | Banner: {banner[:60]}" if banner else ""
        print(f"{Fore.GREEN}  [OPEN]  Port {port:<6} {service:<15}{banner_text}{Style.RESET_ALL}")