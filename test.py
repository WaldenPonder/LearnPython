import time
import math


def print_time(func):
    def wrap(*args):  # 为了能接收参数
        t1 = time.time()
        res = func(*args)
        print("TIME", time.time() - t1)
        return res  # 返回结果
    return wrap


@print_time
def foo(m: int):
    i = 0
    a = []
    while i <= m:
        a.append(math.sqrt(i))
        i += 1
    return a


a = foo(10000) # 实际调用的是print_time返回的wrap
print(len(a))
