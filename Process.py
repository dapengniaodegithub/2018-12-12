from multiprocessing import *
from time import sleep,ctime
class Myprocess(Process):
    def __init__(self, value):
        self.value=value
        super().__init__()
    def fun(self):
        print("第一步")
    def fun2(self):
        print("第二部")
    def run(self):
        self.fun()
        self.fun2()
p=Myprocess(2)
p.start()
p.join()