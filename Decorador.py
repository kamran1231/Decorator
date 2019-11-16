

from functools import wraps

import time
def calculate_time(any_funct):
    @wraps(any_funct)
    def wrapper_func(*args,**kwargs):
        t1 = time.time()

        returned_func =  any_funct(*args,**kwargs)
        t2 = time.time()
        total_time = t2 - t1
        print(f'this function took {total_time}')
        return returned_func
    return wrapper_func
@calculate_time
def square(n):
    return [i ** 2 for i in range(1,n + 1)]

print(square(10000))