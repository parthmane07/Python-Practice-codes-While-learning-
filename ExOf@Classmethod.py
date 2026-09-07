class Student:
    name = "Anything"

    @classmethod
    def ChangeName(cls, name):
        cls.name = name

s1 = Student()
s1.ChangeName("Parth")

print(s1.name)
print(Student.name)