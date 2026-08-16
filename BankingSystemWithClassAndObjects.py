class Account:

    def __init__(self, acc_no, bal):
        self.acc_no = acc_no
        self.bal = bal

    def debit(self, ammount):
        self.bal = self.bal - ammount
        print(ammount, "was debited")

    def credit(self, ammount):
        self.bal = self.bal + ammount
        print(ammount, "was credited")

    def GetBal(self):
        print("your current balance is:",self.bal)

acc1 = Account(101, 5000)
acc1.credit(4000)
acc1.GetBal()

acc1.debit(6000)
acc1.GetBal()