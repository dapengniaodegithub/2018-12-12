import os,time
from threading import Thread ,Lock
"""
使用多个线程，同时从多个地方拷贝文件的某一部分
最终在本地合并为一个
提示: 1. 判断那些目录下有目标文件
     2. 有几个路径下有，就创建几个线程
     3. 每个线程负责一个路径，要选好下载文件的哪部分
     4. 多个线程下载的内容需要最后为一个文件
"""
urls=[ "/home/tarena/桌面/",
    "/home/tarena/模板/",
    "/home/tarena/音乐/",
    "/home/tarena/图片/",
    "/home/tarena/下载/",
    "/home/tarena/视频/",
    ]
lock=Lock()
file_name=input("Dir:")
explore=[]
for i in urls:
    if os.path.exists(i+file_name):
        explore.append(i+file_name)
path_num=len(explore)
if path_num==0:
    print("没有该文件")
    os._exit(0)
total_size=os.path.getsize(explore[0])
base_size=total_size//path_num+1
target = open(file_name, "wb")
def copy_file(r,count):
    fr=open(r,"rb")
    fr.seek(base_size*count)
    data=fr.read()
    with lock:
        target.seek(base_size*count)
        target.write(data)
count=0
jobs=[]
for r in explore:
    t=Thread(target=copy_file,args=(r,count))
    jobs.append(t)
    t.start()
    count+=1
[i.join() for i in jobs]