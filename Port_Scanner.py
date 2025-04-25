#Port_Scanner Tool

# Import required modules
import socket                      # For creating TCP connections
import concurrent.futures          # For multithreading
import sys                         # For real-time progress output

# ANSI color codes for terminal output formatting
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# Function to format and display the port scan results
def format_port_results(results):
    formatted_results = "Port Scan Results:\n"
    formatted_results += "{:<8} {:<15} {:<10}\n".format("Port", "Service", "Status")
    formatted_results += '-' * 85 + "\n"
    for port, service, banner, status in results:
        if status:  # If the port is open
            formatted_results += f"{RED}{port:<8} {service:<15} {'Open':<10}{RESET}\n"
            if banner:  # If banner data is available
                banner_lines = banner.split('\n')
                for line in banner_lines:
                    formatted_results += f"{GREEN}{'':<8}{line}{RESET}\n"
    return formatted_results

# Attempts to grab banner from open port
def get_banner(sock):
    try:
        sock.settimeout(1)                      # Set timeout for banner reading
        banner = sock.recv(1024).decode().strip()  # Receive and decode banner
        return banner
    except:
        return ""  # Return empty if banner cannot be grabbed

# Scans a single port
def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
        sock.settimeout(1)                                        # Set connection timeout
        result = sock.connect_ex((target_ip, port))               # Try connecting to the port

        if result == 0:  # If port is open
            try:
                service = socket.getservbyport(port, 'tcp')       # Get common service name
            except:
                service = 'Unknown'                               # If service can't be resolved
            banner = get_banner(sock)                             # Try to grab banner
            return port, service, banner, True
        else:
            return port, "", "", False  # Port is closed
    except:
        return port, "", "", False  # Error occurred
    finally:
        sock.close()  # Always close the socket

# Main function that performs port scanning
def port_scan(target_host, start_port, end_port):
    target_ip = socket.gethostbyname(target_host)  # Resolve the hostname to IP address
    print(f"Starting scan on host: {target_ip}")

    results = []  # Store results here
    with concurrent.futures.ThreadPoolExecutor(max_workers=400) as executor:
        # Create and submit scan tasks for each port
        futures = {executor.submit(scan_port, target_ip, port): port for port in range(start_port, end_port + 1)}
        total_ports = end_port - start_port + 1

        # Iterate over completed tasks as they finish
        for i, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            port, service, banner, status = future.result()
            results.append((port, service, banner, status))

            # Display scanning progress
            sys.stdout.write(f"\rProgress: {i}/{total_ports} ports scanned")
            sys.stdout.flush()

    sys.stdout.write("\n")  # Move to new line after scanning
    print(format_port_results(results))  # Print formatted scan results

# Entry point for the script
if __name__ == '__main__':
    target_host = input("Enter your target IP or domain: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    port_scan(target_host, start_port, end_port)  # Begin scanning process
