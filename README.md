# Port_Scanner Tool 

## 🎯 Objective

The Port Scanner Tool is designed to identify open TCP ports on a target host using multithreaded scanning for faster results. It not only detects open ports but also attempts to retrieve service names and grab banners, offering insights into which services are exposed. This tool is useful for system administrators and penetration testers to audit exposed services and strengthen security postures.

### 🧠 Skills Learned

- Socket programming in Python for low-level network communication.
- Implementing multithreading using concurrent.futures to scan ports concurrently.
- Service enumeration and banner grabbing to identify exposed services.
- Working with ANSI escape codes for colored console output.
- Real-time terminal progress updates during scanning.

### 🛠 Tools Used

- **socket** module for creating and managing TCP connections.socket module for creating and managing TCP connections.
- **concurrent.futures** for threading to accelerate the scan.
- **ANSI** escape codes for enhanced terminal formatting.
- Basic I/O functions for user interaction and output display.

## 🛠 Step-by-Step Code Breakdown

### **Step 1**: Import Required Modules.
Import **socket** for TCP scanning, **concurrent.futures** for multithreading, and **sys** for progress output.
```python
import socket 
import concurrent.futures
import sys

```

### **Step 2**: Define ANSI Colors for Output Formatting.
  These are used to colorize the console output for better readability.
```python
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
```

### **Step 3**: Format Final Port Scan Output.
This function organizes and prints the results in a table format with color-coded rows for open ports and service banners.
```python
  def format_port_results(results):
      ...
```

### **Step 4**: Banner Grabbing Function.
 Attempts to receive and decode banner info from open ports. Useful for identifying exposed services.
```python
      def get_banner(sock):
        ...

```

### **Step 5**: Port Scanning Function.
  - Connects to a specific port and checks if it's open.
  - If open, tries to identify the service and grab the banner.
```python
     def scan_port(target_ip, port):
        ...
```

### **Step 6**: Main Port Scan Routine.
   - Resolves the hostname to an IP address.
   - Uses a thread pool to scan a large number of ports quickly.
   - Tracks and displays real-time scanning progress.
```python
      def port_scan(target_host, start_port, end_port):
        ...
```

### **Step 7**:  Script Entry Point and User Input
  - Takes target IP and port range from user input and initiates the scan.
```python
     if __name__ == '__main__':
        ...
```


## 🛠 File Structure
```
│
└── port_scanner.py     # Python script for scanning ports and identifying services

```

## 📖 Overall Explanation 
```
This Port Scanner Tool efficiently scans a range of ports on a target host to discover which ones are open and what services may be running behind them. It uses TCP connection attempts via the socket module and performs banner grabbing where possible to provide additional insight. The use of multithreading significantly speeds up the scanning process, making it practical for wide port ranges. With color-coded and formatted output, it provides a clear view of potentially exposed services on the network.
```

## ⚠️ Disclaimer

This tool is intended for educational and authorized testing purposes only.
Do not use it to scan external systems or networks without explicit permission.
Unauthorized scanning is considered illegal and unethical.


## 👤 Author

Made with curiosity and caffeine ☕  
**Gumbo**  
[GitHub Profile](https://github.com/your-username)
