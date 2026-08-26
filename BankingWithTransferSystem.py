class Account:

    def __init__(self, name, acc_no, bal):
        self.name = name
        self.acc_no = acc_no
        self.bal = bal

    def withdraw(self, amount):
        if amount > self.bal:
            print("Insufficient balance(",amount,")to withdraw from",self.name)
        else:
            self.bal = self.bal - amount
            print(amount, "was withdrawed from",self.name)

    def diposit(self, amount):
        self.bal = self.bal + amount
        print(amount, "was diposited to", self.name)

    def display(self):
        print(self.name, self.acc_no, self.bal)

    def transfer(self, other_acc, amount):
        if amount > self.bal:
            print("Insufficient balance(",amount,")to transfer money to",other_acc.name)
        else:
            self.bal = self.bal - amount
            other_acc.bal = other_acc.bal + amount
            print(amount,"was trasfered from", self.name, "to", other_acc.name)


acc1 = Account("Parth", 101, 50000)
acc2 = Account("Tanu", 102, 70000)
acc3 = Account("Nikhil", 103, 40000)

acc1.diposit(20000)
acc2.withdraw(80000)
acc3.transfer(acc1, 50000)

acc1.display()
acc2.display()
acc3.display()

def highest_bal(accounts):
        highest = accounts[0]
        for i in accounts:
            if i.bal > highest.bal:
                highest = i
        return highest

print("Richest account is:")
highest_bal([acc1,acc2,acc3]).display()