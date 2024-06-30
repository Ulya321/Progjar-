import socket
import ssl
from multiprocessing import Process

class SecureHTTPServerProcess(Process):
    def run(self):
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile='server.crt', keyfile='server.key')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
            sock.bind(('0.0.0.0', 443))
            sock.listen(5)
            with context.wrap_socket(sock, server_side=True) as ssock:
                while True:
                    conn, addr = ssock.accept()
                    with conn:
                        print('Connection from', addr)
                        data = conn.recv(1024)
                        if data:
                            # Decode data from bytes to str for processing
                            data_str = data.decode('utf-8')
                            print(f"Data from client: {data_str}")
                            # Process the request and prepare a response
                            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"
                            # Encode response from str to bytes before sending
                            conn.sendall(response.encode('utf-8'))

if __name__ == '__main__':
    server = SecureHTTPServerProcess()
    server.start()
    server.join()
