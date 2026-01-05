def greet(name):
    if(name=="" or name==None): return f"hi user"
    return f"hi {name}"


print(greet(""))


# default parameter if name is never given a value it automatically takes user a default value 
def Default_greet(name="user"):
    return f"hi {name}"



print(Default_greet("londe"))
print(Default_greet())