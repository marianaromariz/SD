from socket import *

placa = input ("Informe a placa:")

if (len(placa) ==7):

	s = socket()
	meusbytes = str.encode(placa,"UTF-8")
	s.connect(("192.168.0.20",8727))
	s.send(meusbytes)
	data = s.recv(1024)
	print ("STATUS: PLACA "+data.decode("utf-8"))
	s.close()
else:
	print("!!! ERRO !!! A placa deve conter 7 caracteres!")

