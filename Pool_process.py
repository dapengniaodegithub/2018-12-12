from multiprocessing import Pool
from time import time,sleep


def worker(msg):
    sleep(2)
    print(time(),"===========",msg)

pool_01=Pool()


for i in range(10):
    msg="Tude %d"%i
    # pool_01.apply_async(func=worker,args=(msg,))
    pool_01.apply_async(worker,args=(msg,))

pool_01.close()
pool_01.join()