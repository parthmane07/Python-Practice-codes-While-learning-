class BankAccount:

    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, ammount):
        self.balance = self.balance + ammount
        return ammount

    def withdraw(self, ammount):
        self.balance = self.balance - ammount
        return ammount

    def GetBal(self):
        return self.balance


acc1 = BankAccount("Parth", 3000)
acc2 = BankAccount("Tanu", 5000)
acc3 = BankAccount("Nikhil", 4000)

acc1.deposit(2000)
acc1.withdraw(500)

acc2.deposit(1000)
acc2.withdraw(500)

acc3.deposit(3000)
acc3.withdraw(1000)

def RichAcc(accounts):
    richest = accounts[0]
    for i in accounts:
        if i.GetBal() > richest.GetBal():
            richest = i

    return richest


print("Richest aacount:", RichAcc([acc1, acc2, acc3]).acc_holder)
print("Balance:", RichAcc([acc1, acc2, acc3]).balance)