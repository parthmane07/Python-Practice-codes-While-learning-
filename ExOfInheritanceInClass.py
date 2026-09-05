class Car:

    color = "black"
    @staticmethod
    def start():
        print("car started...")

class ToyotaCar(Car):

    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("Fortuner")

print(car1.start())