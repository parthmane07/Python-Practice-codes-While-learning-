class Student:
    clg_name = "COCSIT"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def welcome(self):
        print("Welcome", self.name)
        print("Your age is", self.age)
        print("student of", Student.clg_name)

s1 = Student("Tanu", 18)
s1.welcome()

s2 = Student("Parth", 19)
s2.welcome()