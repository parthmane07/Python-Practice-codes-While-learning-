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

    def percentage(self):
        per = self.total() / 5

        return per

    def grade(self):
        if self.percentage() >= 90:
            grade = "A"
        elif  89 >= self.percentage() >= 75:
            grade = "B"
        elif 74 >= self.percentage() >= 60:
            grade = "C"
        elif 59 >= self.percentage() >= 40:
            grade = "D"
        else:
            grade = "F"

        return grade

    def display_result(self):
        return (self.name,
        self.roll_no,
        self.marks,
        self.total(),
        self.percentage(),
        self.grade()
    )


s1 = Student("Tanu",101,[85,75,60,40,50])

print(s1.display_result())