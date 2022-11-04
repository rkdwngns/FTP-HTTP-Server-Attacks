import socket 
s = socket.socket()

addr = ("127.0.0.1", 21)

s.connect(addr)

data = s.recv(1024)

print(data.decode()) # 배너 출력 s.close()
