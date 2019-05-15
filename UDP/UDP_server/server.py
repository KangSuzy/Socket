import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('172.20.10.4',8080))
data, addr = sock.recvfrom(200)

print("received data: ", data.decode().upper())
print("client IP: ", addr[0])
print("client Port: ", addr[1])