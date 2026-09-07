class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        per = (self.phy + self.chem + self.math) / 3

        return per

s1 = Student(90, 90, 90)
print(s1.percentage)

s1.phy = 75
print(s1.percentage)