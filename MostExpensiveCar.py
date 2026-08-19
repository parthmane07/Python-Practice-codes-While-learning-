class Car:

    def __init__(self, brand, model, price, fuel):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel = fuel

    def start(self):
        print("Car started...")

    def stop(self):
        print("Car stopped")

    def disccount(self, percent):
        dis = self.price * (percent/100)
        self.price = self.price - dis
        print("Price of",self.brand, self.model, "after disccount is:", self.price)
        return self.price

    def display(self):
        print(self.brand, self.model, self.price, self.fuel)
        

c1 = Car("Toyota", "Fortuner", 4000000, "Diesel")
c2 = Car("Honda", "City", 1500000, "Petrol")
c3 = Car("Tata", "Nexon", 1200000, "Petrol")

c1.display()
c1.disccount(30)

c2.display()
c2.disccount(20)

c3.display()
c3.disccount(10)

def MostExpensive(cars):
    expensive = cars[0]
    for i in cars:
        if i.price > expensive.price:
            expensive = i

    return expensive

MostExpensive([c1, c2, c3]).display()