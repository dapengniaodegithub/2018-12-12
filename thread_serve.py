from threading import Thread
from socket import *
import os


def handle(c):
    while True:
        data = c.recv()
        if not data:
            break
        print(data.decode())
        c.send(b"ok")
HOST='0.0.0.0'
POST=9999
ADDR=(HOST,POST)
t=Thread
s=socket()
s.bind(ADDR)
s.listen(3)
while True:
    try:
       c,addr=s.accept()
       print("connect from..",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception:
        continue
    t=Thread(target=handle,args=(c,))
    t.setDaemon(True)
    t.start()
