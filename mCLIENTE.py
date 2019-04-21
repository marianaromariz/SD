from socket import  *
import threading
import sys

def recebe():
        while True:
                data = s.recv (4096)
                print (data.decode('UTF-8'))        

s = socket ()

servidor="192.168.0.20"
porta=8752

s.connect((servidor, porta))
t = threading.Thread(target=recebe,args=())
t.start()

while True:
        ss = input (" - ")
        if (ss != ''):
                s.send (str.encode(ss , "UTF-8"))

s.close ()
