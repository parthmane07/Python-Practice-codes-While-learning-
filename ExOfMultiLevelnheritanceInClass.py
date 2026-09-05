class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started...")

class ToyotaCar(Car):
    color = "black"
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("Petrol")

print(car1.start())
print(car1.color)
print(car1.type)