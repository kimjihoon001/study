# generator2.py

import time

def longtime_job():
    print('job start')
    time.sleep(1)   #1초 지연
    return "done"

list_job = (longtime_job() for i in range(5))
print(next(list_job))
print(next(list_job))
print(next(list_job))