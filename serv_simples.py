from socket import *
from threading import Thread

def atende (conn, cliente):
	while True:
		data = conn.recv(4096)
		if not data or len(data) == 0:
			break
		conn.send(str.encode("voce esta conectado", "UTF-8"))
	print ("Fim de conexão com "+str(cliente))
	conn.close

s = socket()

host = "192.168.0.20"
porta = 8752
s.bind((host, porta))
s.listen (10)

while True:
	(conn, cliente) = s.accept()
	t = Thread (target = atende, args = (conn, cliente,))
	t.start()
		
