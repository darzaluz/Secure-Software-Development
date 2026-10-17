import socket 
import ssl

HOST = "localhost"
PORT = 8443 

context = ssl.create_default_context(cafile="server.crt")
context.check_hostname = True
context.verify_mode = ssl.CERT_REQUIRED

with socket.create_connection((HOST, PORT)) as client_socket:
	with context.wrap_socket(client_socket, server_hostname=HOST) as secure_socket:
		print("TLS connection established")
		print("Server certificate verified")

		message = "Hello from the secure client" 
		secure_socket.sendall(message.encode())

		response = secure_socket.recv(1024).decode()
		print("Server response:", response)
