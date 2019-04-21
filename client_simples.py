from socket import *

text = input("Mensagem:")

if(text != ''):

	s = socket()

	meusbytes = str.encode(text, "UTF-8")
	print(meusbytes)

	s.connect(("192.168.0.20",8752))
	s.send(meusbytes)
	data = s.recv (1024)
	print (data.decode("utf-8"))

	s.close()

else:
	print("Digite algo")
