# implemet a decorator that caches the return value of a function so that when the same function is 
# called with same parameters then cached is returned instead of re executing the function again 

import time

def cache(func):
    cached_result={}
    print("cached result \n")
    print(cached_result)
    def wrapper(*args,**kwargs):
        if args in cached_result:
            print(f"cached hit {cached_result[args]}")
            return cached_result[args]
        else:
            result=func(*args,**kwargs)
            cached_result[args]=result
            return result
    return wrapper


def Sum(a,b):
    return a+b

@cache
def func1(a,b):
    time.sleep(2)
    return Sum(a,b)

print(func1(2,2))
print(func1(2,3))
print(func1(2,2))


