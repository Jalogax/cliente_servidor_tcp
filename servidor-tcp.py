import socket

host = '127.0.0.1'
port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Servidor escuchando en {host}:{port}...")

while True:
    conn, addr = server_socket.accept()
    print(f"Conexión establecida con {addr}")

    try:
        conn.sendall("¡Hola, cliente! Envía un mensaje.".encode('utf-8'))

        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break  # Si el cliente se desconecta, salir del bucle.

            print(f"Recibido del cliente: {data}")
            
            # Convertir a mayúsculas y devolver al cliente.
            respuesta = data.upper()
            conn.sendall(respuesta.encode('utf-8'))

            # Si el cliente envía "DESCONEXION", se cierra la conexión.
            if data.upper() == "DESCONEXION":
                print(f"Servidor cierra la conexión con el cliente {addr}.")
                break

    except Exception as e:
        print(f"Error inesperado con {addr}: {e}")

    finally:
        conn.close()  # Se cierra solo la conexión con este cliente, pero el servidor sigue activo.
