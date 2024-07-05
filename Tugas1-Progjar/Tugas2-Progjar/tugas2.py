import socket
import threading
import datetime

# Fungsi untuk menangani setiap klien
def handle_client(client_socket):
    try:
        while True:
            # Menerima data dari klien
            request = client_socket.recv(1024).decode('utf-8')
            print(f"Diterima: {request}")  # Debugging
            
            # Mengecek apakah request diawali dengan "TIME" dan diakhiri dengan karakter 13 dan 10
            if request.startswith("TIME") and request.endswith("\r\n"):
                # Mendapatkan waktu saat ini dalam format "hh:mm:ss"
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                response = f"JAM {current_time}\r\n"
                print(f"Respon: {response}")  # Debugging
                # Mengirim respon ke klien
                client_socket.send(response.encode('utf-8'))
            # Mengecek apakah request adalah "QUIT" dan diakhiri dengan karakter 13 dan 10
            elif request.startswith("QUIT") and request.endswith("\r\n"):
                break
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        client_socket.close()

# Fungsi utama untuk menjalankan server
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("172.16.16.101", 45002))  # Pastikan menggunakan port yang benar
    server.listen(5)
    print("Server berjalan di port 45001")

    while True:
        # Menerima koneksi dari klien
        client_socket, addr = server.accept()
        print(f"Terhubung dengan {addr}")
        # Membuat thread baru untuk menangani klien
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
