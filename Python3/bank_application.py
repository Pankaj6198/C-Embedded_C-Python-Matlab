class Customer:
    """ Customer class for demo purpose """
    bankname="People's Bank of india"
    def __init__(self,name,balance=0.00):  # Default Argument, default value Balance = 0.00 , balance at opening of the account will be zero..
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited Amount:",amount,"\tTotal balance:",self.balance)
        print()
    def withdraw(self,amount):
        if amount > self.balance:
            print("\nInsufficient balance in your account !!! ")
        else:
            self.balance-=amount
            print("withdrawal amount:",amount,"\tTotal balance:",self.balance)

print("Welcome to",Customer.bankname) # accessing static variable (bankname)
name=input("Enter Name: ")
c=Customer(name) # balance default argument with default value 0.00
while True:
    option=input(" MENU :\n D - Deposite\n W - Withdraw\n E - Exit\n\n")
    if option.lower()=='d':
        amount=float(input("Enter amount to be deposited:"))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float(input("Enter amount to be deposited:"))
        c.withdraw(amount)
    elif option.lower()=='e':
        print("\nThanks for using",Customer.bankname,"banking portal ....")
        break
    else:
        print("\n Invalid choice !!! Please choose a valid option...")