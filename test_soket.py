import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8001))
# server = socket.create_server(('127.0.0.1', 8001)) 
server.listen(4)
print('Working...')
client_soket, adress = server.accept()
data = client_soket.recv(1024).decode('utf-8')
print(data)
content = 'Hello word!'.encode('utf-8')
client_soket.send(content)