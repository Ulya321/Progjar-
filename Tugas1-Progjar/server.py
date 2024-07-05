import socket
import logging

logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the port
    server_address = ('172.16.16.101', 32444)  # Use 127.0.0.1 instead of localhost
    logging.info(f"starting up on {server_address}")
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)
    logging.info("waiting for a connection")
    
    while True:
        logging.info("Ready to accept a connection")
        connection, client_address = sock.accept()
        logging.info(f"connection from {client_address}")
        try:
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(32)
                logging.info(f"received {data}")
                if data:
                    logging.info("sending back data")
                    connection.sendall(data)
                else:
                    logging.info(f"no more data from {client_address}")
                    break
        finally:
            # Clean up the connection
            connection.close()
except Exception as ee:
    logging.info(f"ERROR: {str(ee)}")
finally:
    logging.info('closing')
    sock.close()
