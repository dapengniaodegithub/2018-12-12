from select import select
from socket import *
import time
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8889))
s.listen(3)
# 设置关注的IO

rlist=[s,]# s的读IO行为
wlist=[]
xlist=[]
while True:
    rs,ws,xs=select(rlist,wlist,xlist)#[s,c1,c2]
    for r in rs:#c2
        if r is s:
            c,addr=r.accept()
            print("connect from ...")
            rlist.append(c)
        else:
            data=r.recv(1024).decode()#r=c2
            print(data)
            if not data:
                rlist.remove(r)
                r.close()
            wlist.append(r)

    for n in ws:
        n.send(b'ok')