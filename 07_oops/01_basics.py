# this is the most basic way to work with classes
# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
    
#     def printDetails(self):
#         print(f"{self.brand} {self.model}")
    


# my_car=Car("bmw","100")
# my_car.printDetails()
        

#now we will se encapsulation (private banayenge brand ko)

# class Car:
#     def __init__(self,brand,model):
#         self.__brand=brand
#         self.model=model
    
#     def printDetails(self):
#         print(f"{self.__brand} {self.model}")

# my_car=Car("bmw","100")
# my_car.printDetails()
# print(my_car.model)
# print(my_car.brand)

# now we will see inheritance 

class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
    
    def printDetails(self):
        print(f"{self.__brand} {self.__model}")

    def get_brand(self):
        return self.__brand
    
    @staticmethod
    def general_description():
        return f"cars general description"
    
    @property
    def model(self):
        return self.__model
    


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        self.battery_size=battery_size
        super().__init__(brand,model)


myev=ElectricCar("tesela","100","85khz")
print(myev.battery_size)
myev.printDetails()
print(myev.get_brand())
print(Car.general_description())

print(myev.model)
# myev.model="200"
print(myev.model)


# my_car=Car("bmw","100")
# my_car.printDetails()
# print(my_car.model)
# print(my_car.brand)