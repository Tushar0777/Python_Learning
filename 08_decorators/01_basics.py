import time

def timer(func):
    def wrapper(*args,**kwargs):
        start =time.time()
        result=func(*args,**kwargs)
        end=time.time()

        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper


@timer
def Delay_timer(n):
    print(f"timer sleep started ")
    time.sleep(n)
    print(f"timer sleep ends")


ex=Delay_timer(2)
# isme dekh @timer lagane ke baad Delay_timer call krne ke baad bhi timer se hoke ja rha hau mtlb 
# phele timer run hoga timer khud as argument/parameter ek function ko leta hai 


