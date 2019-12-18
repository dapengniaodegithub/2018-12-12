import os
from time import sleep
a=1
id=os.fork()

if id==0:
    a=100
    print("child",a)

elif id>0:
    sleep(1)
    print("parents",a)
print(a)