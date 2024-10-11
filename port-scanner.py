import socket
import threading
import queue

# Objective: 
# This script will scan a given IP address for open ports. It will use multithreading to speed up the scanning process.

# Function to scan a single port
def scan_port(ip, port, result_queue):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(0.5)
        # Attempt to connect to the target IP and port
        result = sock.connect_ex((ip, port))
        # If the connection succeeds, the port is open
        if result == 0:
            result_queue.put(port)
        # Close the socket
        sock.close()
    except:
        pass

# Function to scan a range of ports
def scan_ports(ip, start_port, end_port, num_threads):
    # Create a queue to hold the results
    result_queue = queue.Queue()
    # Create a list to hold the threads
    threads = []
    
    # Create a thread for each port
    for port in range(start_port, end_port+1):
        t = threading.Thread(target=scan_port, args=(ip, port, result_queue))
        threads.append(t)
        t.start()
    
    # Wait for all threads to finish
    for t in threads:
        t.join()
    
    # Get the results from the queue
    open_ports = []
    while not result_queue.empty():
        port = result_queue.get()
        open_ports.append(port)
    
    return open_ports

# Main function to run the port scanner
def main():
    # Prompt the user for the target IP address and port range
    ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    num_threads = int(input("Enter the number of threads to use: "))
    
    # Scan the ports
    open_ports = scan_ports(ip, start_port, end_port, num_threads)
    
    # Print the open ports
    print(f"Open ports on {ip}:")
    for port in open_ports:
        print(port)

# Run the main function
if __name__ == "__main__":
    main()