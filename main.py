class Atm:
    def __init__(self):
        self.__code=""
        self.__balance=0
        self.menu()

    def menu(self):
        user= input('''
    Welcome to Our ATM!
    Press '1' to set pin
    Press '2' to change pin
    Press '3' to deposit money
    Press '4' to check balance
    Press '5' to withdraw money
    Press '6' to exit \n
''')
        if user=='1':
            self.pin()
            self.menu()
        elif user=='2':
            self.changePin()
            self.menu()
        elif user=='3':
            self.depositMoney()
            self.menu()
        elif user=='4':
            self.checkBalance()
            self.menu()
        elif user=='5':
            self.withdrawMoney()
            self.menu()
        elif user=='6':
            print("Thank You for choosing our service!")
            exit()

    def pin(self):
        self.__code=input("Enter you pin: ")
        print("Pin is set successfully!")

    def changePin(self):
        self.checkpin= input("Enter you existing pin: ")
        if self.checkpin==self.__code:
            self.__code=input("Enter your new pin: ")
            print("Pin changed successfully!")
        else:
            print("Pin doesnot matched!")

    def depositMoney(self):
        self.checkpin= input("Enter you existing pin: ")
        if self.checkpin==self.__code:
            self.temp__balance=int(input("Enter the amout: "))
            self.__balance +=self.temp__balance
            print("Amount Deposited successfully!")
        else:
            print("Pin doesnot matched!")

    def checkBalance(self):
        print(f"The current amount in your bank account is {self.__balance}")

    def withdrawMoney(self):
        self.checkpin= input("Enter you existing pin: ")
        if self.checkpin==self.__code:
            self.withdraw=int(input("Enter the amount to withdraw: "))
            if self.withdraw<=self.__balance:
                self.__balance-=self.withdraw
                print(f"Balance {self.withdraw} is sucessfully withdrawn!")
            else:
                print("Insufficient Balance in you account!")
        else:
            print("Pin doesnot matched!")

subhradip= Atm()
