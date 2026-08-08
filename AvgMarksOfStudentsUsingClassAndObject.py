class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def avarage(self):
        avg = (self.phy + self.chem + self.bio)/3

        return avg

s1 = Student("Parth", 80, 60, 100)
s2 = Student("Tanu", 70, 90, 40)

print("Avg of marks of",s1.name ,"is", s1.avarage())
print("Avg of marks of", s2.name,"is", s2.avarage())