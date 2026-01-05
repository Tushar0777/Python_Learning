username="chai aur code "

def func():
    username="chai "
    print(username)

print(username)
func()
print(username)



def f1(num):
    def actual(n):
        return n**num
    return actual

square=f1(2)
cube=f1(3)

print(square(2))
print(cube(3))