import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0",8080))
s.listen(10)

conn, address = s.accept()
print(str(conn.recv(4096)))

conn.close()
s.close()