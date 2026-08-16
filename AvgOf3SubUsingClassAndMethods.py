class student:
    
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def AvgMarks(self):
        avg = (self.phy + self.chem + self.bio)/3
        print("The avg of", self.name,"'s marks is:", avg)


s1 = student("Tanu", 60, 70, 80)
s1.AvgMarks()