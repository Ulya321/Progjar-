import socket
import logging

# Set basic logging
logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('172.16.16.101',32444)  # Use 127.0.0.1 instead of localhost
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    # Send data
    message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    logging.info(f"sending {message}")
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        logging.info(f"received {data.decode()}")
        
except Exception as ee:
    logging.info(f"ERROR: {str(ee)}")
finally:
    logging.info("closing")
    sock.close()
