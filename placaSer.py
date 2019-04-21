from socket import *
from threading import Thread

def valida_placa(placa):
	placa_m = placa.upper()
	if((ord(placa_m[0])>=65) and (ord(placa_m[0]) <= 90)):
		if((ord(placa_m[1])>=65) and (ord(placa_m[1]) <= 90)):
			if((ord(placa_m[2])>=65) and (ord(placa_m[2]) <= 90)):
				if((ord(placa_m[3])>=48) and (ord(placa_m[3]) <= 57)):
					if((ord(placa_m[4])>=65) and (ord(placa_m[4]) <= 90)):
						if((ord(placa_m[5])>=48) and (ord(placa_m[5]) <= 57)):
							if((ord(placa_m[6])>=48) and (ord(placa_m[6]) <= 57)):
								return "VÁLIDA"
	return "INVÁLIDA"
def atende (conn, cliente):
	while True:
		data= conn.recv(4096)
		if not data or len(data) == 0:
			break
		conn.send(str.encode(valida_placa(data.decode("utf-8")), "UTF-8"))
	print ("Fim de conexão com "+str(cliente))
	conn.close
s = socket()

host = "192.168.0.20"
porta = 8727
s.bind((host, porta))
s.listen (10)

while True:
	(conn, cliente) = s.accept()
	t = Thread (target = atende, args = (conn, cliente,))
	t.start()
		
