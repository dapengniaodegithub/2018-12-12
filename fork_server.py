"""
基于fork的多进程服务
"""
from  socket import *
import os
import signal
#全局变量
def handle(c):
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok")
    c.close()
HOST="0.0.0.0"
POST=8889
ADDR=(HOST,POST)
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("Listen the port 8888...")
while True:
    #循环接受来自客户端的链接
    try:
        c,addr=s.accept()
        print("Connect from...",addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    #客户端连接处理
    pid=os.fork()
    if pid==0:
        s.close()
        handle(c)
        os._exit(0)
    else:
        c.close()