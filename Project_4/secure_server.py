import socket 
import ssl 

HOST = "localhost"
PORT = 8443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
	server_socket.bind((HOST, PORT))
	server_socket.listen(1)

	print(f"Secure server listening on {HOST}:{PORT}")

	with context.wrap_socket(server_socket, server_side=True) as secure_socket:
		connection, address = secure_socket.accept()

		with connection: 
			print("Secure connection established with:" , address)

			message = connection.recv(1024).decode()
			print("Received:", message)

			response = "Secure message received"
			connection.sendall(response.encode())

