# Port Scanner in Python

## Objective

The objective of this project is to create a port scanner in Python that can scan a given IP address for open ports. The script uses multithreading to speed up the scanning process by creating separate threads for each port scanning attempt. The queue module is used to safely exchange results between threads.

The script prompts the user for the target IP address, starting port, ending port, and the number of threads to use. It then scans the specified range of ports and prints the open ports to the console.

This script can be useful for network administrators, security researchers, and anyone else who needs to quickly identify open ports on a target system.

### Explanation

- The script starts by importing the necessary modules: `socket`, `threading`, and `queue`.
    
- The `scan_port` function is defined to scan a single port. It takes the target IP address, port number, and a result queue as arguments. Inside the function:
    
    - A socket object is created with the `AF_INET` (IPv4) and `SOCK_STREAM` (TCP) protocols.
    - The socket timeout is set to 0.5 seconds.
    - An attempt is made to connect to the target IP and port using the `connect_ex` method.
    - If the connection succeeds (result is 0), the port is considered open and added to the result queue.
    - The socket is closed.
- The `scan_ports` function is defined to scan a range of ports. It takes the target IP address, starting port, ending port, and the number of threads to use as arguments. Inside the function:
    
    - A queue is created to hold the results.
    - A list is created to hold the threads.
    - For each port in the specified range, a new thread is created that calls the `scan_port` function with the current port.
    - The threads are started.
    - The main thread waits for all threads to finish using the `join` method.
    - The results from the queue are retrieved and stored in the `open_ports` list.
    - The `open_ports` list is returned.
- The `main` function is the entry point of the script. It prompts the user for the target IP address, starting port, ending port, and the number of threads to use.
    
    - The user input is validated and converted to the appropriate data types.
    - The `scan_ports` function is called with the provided parameters.
    - The open ports are printed to the console.
- The script is set to run the `main` function when executed as the main program.

