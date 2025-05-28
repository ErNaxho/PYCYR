import socket

def start_chat():
    # Configuración del servidor
    host = input("Ingrese la dirección IP del servidor (o deje en blanco para actuar como servidor): ")
    port = 12345  # Puerto fijo para la comunicación

    if not host:
        # Actuar como servidor
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("", port))
        server_ip = socket.gethostbyname(socket.gethostname())
        print(f"El servidor está corriendo en la IP: {server_ip}")
        server_socket.listen(1)
        print("Esperando conexión...")
        conn, addr = server_socket.accept()
        print(f"Conexión establecida con {addr}")

        while True:
            message = input("Tú: ")
            conn.sendall(message.encode())
            if message.lower() == "salir":
                print("Cerrando conexión...")
                break

            data = conn.recv(1024).decode()
            if data.lower() == "salir":
                print("El cliente ha cerrado la conexión.")
                break
            print(f"{addr}: {data}")

        conn.close()
        server_socket.close()
    else:
        # Actuar como cliente
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("Conexión establecida con el servidor.")

        while True:
            data = client_socket.recv(1024).decode()
            if data.lower() == "salir":
                print("El servidor ha cerrado la conexión.")
                break
            print(f"Servidor: {data}")

            message = input("Tú: ")
            client_socket.sendall(message.encode())
            if message.lower() == "salir":
                print("Cerrando conexión...")
                break

        client_socket.close()

if __name__ == "__main__":
    start_chat()