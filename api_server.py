import socket

# 1. Set up the "kitchen" to listen on its private network
HOST = '0.0.0.0'  # Listens on all available interfaces inside the container
PORT = 9999       # The port the kitchen is listening on

print("--- API Server (Kitchen) is starting up... ---")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"--- Kitchen is open and listening for orders on port {PORT} ---")
    
    # 2. Wait for a customer (client) to connect
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr} (a new diner has sat down)")
        
        # 3. Receive the API call (the order)
        data = conn.recv(1024)
        if data:
            message = data.decode('utf-8')
            print(f"Received API Call (Order): '{message}'")
            
            # 4. Send a response
            conn.sendall(b"Order Received! (This is the API response)")
            
print("--- Kitchen is closing for the day. ---")