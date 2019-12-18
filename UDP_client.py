from socket import *
from struct import *
sockfd=socket(AF_INET,SOCK_DGRAM)
st = Struct("i20sif")
ADDR=('176.47.7.13',9998)
while True:
    id=int(input("请输入学生id"))
    name=input("请输入学生姓名:").encode()
    age=int(input("请输入学生年龄"))
    score=float(input("请输入分数"))
    n=st.pack(id,name,age,score)
    #向服务端发送消息
    sockfd.sendto(n,ADDR)
    msg,addr=sockfd.recvfrom(1024)
    print("from server:",msg.decode())
    print(addr)
sockfd.close()

jhgvhkgvk
