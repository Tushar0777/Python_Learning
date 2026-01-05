def kwargs_function(**kwargs):
    print(kwargs)
    for key , value in kwargs.items():
        print(f"{key} {value}")


print(kwargs_function(name="tushar" ,soulmate="smridhi"))