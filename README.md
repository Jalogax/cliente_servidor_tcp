# Prueba técnica: Cliente Servidor TCP

El proyecto implementa la creación de un servidor TCP y un cliente TCP en Python, los cuales pueden comunicarse entre
sí en la misma máquina (localhost o 127.0.0.1) usando el puerto 5000.

## Instalación
Para ejecutar este programa, necesitas tener instalado en tu computadora Python, en caso de no tenerlo, puedes realizarlo desde la página:

```bash
https://www.python.org/downloads/
```
Una vez instalado, puedes continuar con la ejecución del programa. En mi caso yo cuento con la versión de Python 3.13.2, pero también debería de funcionar con otras versiones.

Clona el repositorio en una ruta local de tu computadora:
```bash
git clone https://github.com/Jalogax/cliente_servidor_tcp.git
```

## Uso

1. Para iniciar con el servidor, abre la consola dentro de la carpeta del repositorio descargada y ejecuta el siguiente comando:
```bash
py servidor-tcp.py
```

Nota: Esto iniciará el servidor y estará a la espera de conexiones de clientes. La consola debe de mostrar un mensaje como el siguiente:
```bash
C:\Prueba\cliente_servidor_tcp>py servidor-tcp.py
Servidor escuchando en 127.0.0.1:5000...
```


2. Para conectarte como cliente, en otra consola, ejecuta el siguiente comando:
```bash
py cliente-tcp.py
```

Nota: Esto iniciará la conexión del cliente con el servidor y estará a la espera de envío de mensajes para el servidor. La consola debe de mostrar un mensaje como el siguiente:
```bash
C:\Prueba\cliente_servidor_tcp>py cliente-tcp.py
Servidor: ¡Hola, cliente! Envía un mensaje.
Cliente envía:
```

Y listo, ya tendrás tu cliente para envío de mensajes al servidor, y a la vez, al servidor a la espera de conexiones y mensajes de los clientes.

## Pruebas

La primera prueba es enviar el mensaje "hola servidor" desde el cliente, y que el servidor nos responda el mensaje en mayúsculas. Para lo cual, nuestra consola del cliente debe de mostrar esto:
```bash
C:\Prueba\cliente_servidor_tcp>py cliente-tcp.py
Servidor: ¡Hola, cliente! Envía un mensaje.
Cliente envía: hola servidor
Servidor responde: HOLA SERVIDOR
```

Y la segunda, enviar desde la consola del cliente la palabra "DESCONEXION" y que se muestre el mensaje "Servidor cierra la conexión con el cliente." Para lo cual, la consola del cliente nos debe de mostrar esto:
```bash
Cliente envía: DESCONEXION
Servidor responde: DESCONEXION
Servidor cierra la conexión con el cliente.

C:\Prueba\cliente_servidor_tcp>
```

Puedes ver de manera gráfica estas pruebas en el archivo de "Pruebas de cliente servidor TCP.docx" mismo que se encuentra dentro de este repositorio.

