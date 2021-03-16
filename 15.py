class MobileBanking:
    def __init__(self):
        self.balance = 0
        print("Welcome to Mobile Banking!!")

    def customer_info(self):
        name = input("Enter your name please : ")
        self.name = name
        citizenship_no = int(input("Enter last 4digits of your citizenship no: "))
        self.citizenship_no = citizenship_no
        print(f'Hello!! Welcome {self.name}')

    def deposit(self):
        deposit_amt = float(input("Enter amount to be deposited: "))
        self.balance = self.balance + deposit_amt
        print(f'Deposited Amount: {deposit_amt}')

    def withdraw(self):
        withdrawn_amt = float(input("Enter amount to withdraw: "))
        if self.balance > withdrawn_amt:
            self.balance = self.balance - withdrawn_amt
            print(f'Withdrawn Amount: {withdrawn_amt}')
        else:
            print(f'Insufficient Balance')

    def display(self):
        print(f'Net Available Balance: {self.balance}')


m = MobileBanking()
m.customer_info()
m.deposit()
m.withdraw()
m.display()
