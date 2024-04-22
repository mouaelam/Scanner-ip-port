import socket

def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        if scan_port(host, port):
            open_ports.append(port)
    return open_ports

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        s.close()
        if result == 0:
            return True
        else:
            return False
    except socket.error:
        return False

def scan_ip_range(start_ip, end_ip, ports, filename):
    with open(filename, "a") as file:
        for i in range(start_ip[0], end_ip[0]+1):
            for j in range(start_ip[1], end_ip[1]+1):
                for k in range(start_ip[2], end_ip[2]+1):
                    for l in range(start_ip[3], end_ip[3]+1):
                        host = f"{i}.{j}.{k}.{l}"
                        open_ports = scan_ports(host, ports)
                        if open_ports:
                            result = f"Open ports on host {host}: {open_ports}\n"
                            print(result)
                            file.write(result)

# Ask user for IP range
start_ip = input("Enter start IP address (e.g., 192.168.0.0): ").split('.')
end_ip = input("Enter end IP address (e.g., 192.168.255.255): ").split('.')

# Convert to integers
start_ip = list(map(int, start_ip))
end_ip = list(map(int, end_ip))

# Ask user for ports to scan
ports_str = input("Enter ports to scan separated by comma (e.g., 80,443,22): ")
ports = [int(port) for port in ports_str.split(',')]

# Ask user for filename
filename = input("Enter the path to save the results (e.g., C:\\Users\\userName\\Downloads\\ip.txt): ")

# Call the scan_ip_range function
scan_ip_range(start_ip, end_ip, ports, filename)