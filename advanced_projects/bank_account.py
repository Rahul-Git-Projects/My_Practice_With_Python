from os import system

class Person:
    def __init__(self,firstname,last_name):
        self.firstname = firstname
        self.lastname = last_name

class Customer(Person):
    def __init__(self,firstname,lastname,account_number,balance):
        super().__init__(firstname,lastname)
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        self.balance -= amount

def access():
    f_name = input("Welcome to SBI!,Please enter your firstname: ")
    l_name = input("Please enter your lastname: ")
    acc_num = input("Your bank account number: ")
    balance_rem = int(input("Your balance in your account: "))
    print(f"Welcome! {f"{f_name} {l_name}"}\naccount number: {acc_num}\nbalance: {balance_rem}")
    customer = Customer(f_name,l_name,acc_num,balance_rem)
    return customer

def choice():
    print("""
    Enter the number corresponding to the actions given below to execute them:
    1 --> Deposit
    2 --> Withdraw
    3 -- > Exit""")
    user_choice = input("Enter the number here:  ")
    while user_choice not in ["1","2","3"]:
        user_choice = input("Please choose a number between 1 to 3:  ")
    return user_choice

if __name__ == "__main__":
    user = access()
    end_program = False
    while not end_program:
        match choice():
            case "1":
                system("cls")
                deposited_amount = int(input("How much would you like to deposit? : "))
                user.deposit(deposited_amount)
                input("Current balance: {},press enter to go back to main screen".format(user.balance))
            case "2":
                system("cls")
                withdrew_amount = int(input("How much would you like to withdraw? : "))
                if withdrew_amount <= user.balance:
                    user.withdraw(withdrew_amount)
                    input("Current balance: {},press enter to go back to main screen".format(user.balance))
                else: input("Transaction declined,Your withdrawal amount is greater than your remaining balance,\npress enter to go back to main screen")
            case "3":
                end_program = True







