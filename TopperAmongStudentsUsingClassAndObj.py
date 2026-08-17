class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def total(self):
        total = 0
        for i in self.marks:
            total += i

        return total

s1 = Student("Parth", 101, [90,80,70,60,50])
s2 = Student("Tanu", 102, [50,60,70,30,90])
s3 = Student("Nikhil", 103, [10,20,30,40,50])


def top_student(students):
    top_student = students[0]
    for i in students:
        if i.total() > top_student.total():
            top_student = i

    return top_student.name

print(top_student([s1,s2,s3]))