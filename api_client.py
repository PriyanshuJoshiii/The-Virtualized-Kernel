import socket
import time

# The name 'api-server' is the "hostname" of the kitchen.
# Docker's network will automatically route this to the right container.
SERVER_HOSTNAME = 'api-server'
PORT = 9999

print("--- API Client (Diner) is ready to order. ---")
print(f"Waiting for the kitchen ({SERVER_HOSTNAME}) to open...")
time.sleep(5) # Give the server 5 seconds to start up first

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 1. Connect to the kitchen
        s.connect((SERVER_HOSTNAME, PORT))
        
        # 2. Make the API Call (send the order)
        print("Sending API Call (Order): 'GET_USER_DATA'")
        s.sendall(b'GET_USER_DATA')
        
        # 3. Wait for the response
        response = s.recv(1024)
        
        print(f"\nServer Response: '{response.decode('utf-8')}'")

except Exception as e:
    print(f"\nError: Could not connect to the kitchen. {e}")