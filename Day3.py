import time
from threading import Thread
import concurrent.futures as cf
from concurrent.futures import ThreadPoolExecutor


def func_take_time():
    print("Before Sleeping")
    time.sleep(2)
    print("After Sleeping")

# th =Thread(target=func_take_time)
# th.start()
# th.join()
# print("Thread started")

# with ThreadPoolExecutor(max_workers=1) as ex:
#     future = ex.submit(func_take_time)
#     time.sleep(2)
#     print("After sleep calling the result")
#     print(future.done())


def func_take_time(seconds):
    print("Before Sleeping")
    time.sleep(seconds)
    print("After Sleeping")
    return "Done @" + str(seconds)

timer = [2,3]

with ThreadPoolExecutor(max_workers=5) as ex:
    results = ex.map(func_take_time,[the_time for the_time in timer])
    for value in results:
        print(value)