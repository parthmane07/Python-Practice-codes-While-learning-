class Employee:

    def __init__(self, name, empID, salary):
        self.name = name
        self.empID = empID
        self.salary = salary

    def display(self):
        print("Name:", self.name, ",ID:", self.empID, ",Salary:", self.salary)
        

    def raise_salary(self, percent):
        hike = self.salary  * (percent/100)
        self.salary = self.salary + hike
        print("Salary of",self.name, "after hike of",percent,"%is:",self.salary)
        return self.salary


E1 = Employee("Parth", 101, 100000)
E2 = Employee("Tanu", 102, 120000)
E3 = Employee("Nikhil", 103, 90000)

E1.display()
E2.display()
E3.display()

E1.raise_salary(20)
E2.raise_salary(10)
E3.raise_salary(15)

def highest_salary(employee):
    MostPaid = employee[0]

    for i in employee:
        if i.salary > MostPaid.salary:
            MostPaid = i
        
    return MostPaid

print("Most paid emplyee is:")
highest_salary([E1,E2,E3]).display()