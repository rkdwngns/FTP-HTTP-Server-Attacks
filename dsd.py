import socket

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