import socket
import threading

IP = "0.0.0.0"
PORT = 443


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f"[*] conexão estabelecida em {IP}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"[*] conexão recebida de {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[*] Recebido: {request.decode('utf-8')}")
        sock.send(b"ACK")

if __name__ == "__main__":
    main()
