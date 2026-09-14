import socket 

target_host = "google.com" #aqui você pode colocar o ip ou DNS do servidor que você quer se conectar
ltarget_port = 80 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, ltarget_port))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)
print(response.decode())
client.close()