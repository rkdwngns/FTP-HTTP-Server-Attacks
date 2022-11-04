import socket 

s = socket.socket() # 생략하면 TCP 통신

s.connect(("142.251.42.206", 80)) # nslookup google.com

s.send(b"GET / HTTP/1.1\\r\\nhost: google.com\\r\\n\\r\\n") # 네트워크 통신을 위해 바이트 코드로 구성

data = s.recv(1024) 
print(data.decode()) 
s.close()
