from socket import  *

s = socket ()

minhastr = "Ola mundo"
print (minhastr)
meusbytes=str.encode (minhastr, "UTF-8")
print (meusbytes)

s.connect(("192.168.0.20", 8752))
s.send (meusbytes)

data = s.recv (1024)

print (data.decode("utf-8"))

s.close ()
