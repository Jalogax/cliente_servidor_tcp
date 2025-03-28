import socket

host = '127.0.0.1'
port = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((host, port))

    mensaje_inicial = client_socket.recv(1024).decode('utf-8')
    print(f"Servidor: {mensaje_inicial}")

    while True:
        mensaje = input("Cliente envía: ")

        client_socket.sendall(mensaje.encode('utf-8'))  # Se envia mensaje al servidor.

        respuesta = client_socket.recv(1024).decode('utf-8')
        print(f"Servidor responde: {respuesta}")

        # Si el usuario escribe "DESCONEXION", se cierra el cliente.
        if mensaje.upper() == "DESCONEXION":
            print("Servidor cierra la conexión con el cliente.")
            break

finally:
    client_socket.close()
