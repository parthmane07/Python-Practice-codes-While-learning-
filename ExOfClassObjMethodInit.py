class Student:
    clg_name = "COCSIT"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def welcome(self):
        print("Welcome", self.name)
        print("Your age is", self.age)

s1 = Student("Tanu", 18)
s1.welcome()
print(s1.clg_name)

s2 = Student("Parth", 19)
s2.welcome()
print(s2.clg_name)