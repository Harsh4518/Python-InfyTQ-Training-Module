class Account:

    acc_no=2000

    def __init__(self,name):

        self.name=name
        Account.acc_no=Account.acc_no+1
        self.account_no=Account.acc_no

a1=Account("Binod")
a2=Account("Manoj")
a3=Account("John")

print(a1.account_no)
print(a2.account_no)
print(a3.account_no)
print(Account.acc_no)
print(a1.acc_no)
a1.acc_no=2000
print(a1.acc_no)
