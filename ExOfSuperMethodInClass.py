class College:
    def __init__(self, clg_name):
        self.clg_name = clg_name

class Class(College):
    def __init__(self, course, clg_name):
        self.course = course
        super().__init__(clg_name)

class Student(Class):
    def __init__(self, name, clg_name, course):
        self.name = name
        super().__init__(course, clg_name)

s1 = Student("Parth", "COCSIT", "BCA")

print(s1.name)
print(s1.clg_name)
print(s1.course)