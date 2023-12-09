#MINIPROJECT_ONLINE BANKING SYSTEM_USING CLASSES AND OBJECT

#DISPLAY
print("\t\t\t\t****************************")
print("\t\t\t\t\tONLINE BANKING SYSTEM")
print("\t\t\t\t****************************")

# BANK CLASS WITH FUNCTION FOR CHECKING BALANCE, DEPOSITING AND WITHDRAWAL of CASH,PASSWORD CHANGE
class Bank():
    # Dictionary for customer details
    customer_data = {
        "Aseela": {"password": "asi1234", "balance": 10000, "phone no": 9496817137},
        "Ajish": {"password": "aji1234", "balance": 5000, "phone no": 9496758871},
        "Anish": {"password": "ani1234", "balance": 16000, "phone no": 9448875324},
        "Aljuwad": {"password": "alju1234", "balance": 9000, "phone no": 9447698883}
    }

#FUNCTION FOR CHECKING BALANCE AMOUNT
    def balance(self):
        bal=self.customer_data[user_name]["balance"]
        print(f"Your account balance is:Rs.{bal}")

#FUNCTION FOR WITHDRAWING AMOUNT
    def withdraw(self):
        try:
            withdraw_amount = int(input("-----------Withdraw-----------\nHow much would you like to withdraw? "))
            bal = self.customer_data[user_name]["balance"]
            if withdraw_amount >= bal:
                print("Insufficient balance")
            else:
                bal = bal - withdraw_amount
                newbalance=bal
                self.customer_data[user_name]["balance"]=newbalance
                print(f"\nRs.{withdraw_amount} is debited from your account\nThe current account balance is Rs.{newbalance}")
        except ValueError:
            print("Error: Please enter a number (without signs)\n")

#FUNCTION TO DEPOSIT AMOUNT
    def deposit(self):
        try:
            deposit_amount = int(input("-----------Deposit-----------\nHow much would you like to deposit? "))
            bal = self.customer_data[user_name]["balance"]
            bal= bal+deposit_amount
            newbalance = bal
            self.customer_data[user_name]["balance"] = newbalance
            print(f"\nRs.{deposit_amount} is credited to your account\nThe current account balance is Rs.{newbalance}")
        except ValueError:
            print("Error: Please enter a number (without signs)\n")

#FUNCTION TO CHANGE PASSWORD
    def changepassword(self):
        new_password1=input("Enter your new password\t:")
        new_password2=input("Re enter your password\t:")

        if new_password1 == new_password2:
            self.customer_data[user_name]["password"] = new_password1
            print("Password changed successfully!")
        else:
            print("Password entered do not match. Try again")


bank= Bank()    #object created to access bank claass methods


#FUNCTION TO DISPLAY THE MENU
def menu():
    while True:
        user_response=int(input(("-----------Choose your option-------------\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Quit\n")))
        if user_response == 1:
            bank.balance()
        elif user_response == 2:
            bank.withdraw()
        elif user_response == 3:
            bank.deposit()
        else:
            print("\nGood bye!")
            break

#ACCOUNT LOGIN
while True:
    print("******Welcome to the Bank******")
    user_name=input("Enter your username\t:")
    pass_word=input("Enter your password\t:")

    if user_name in bank.customer_data and bank.customer_data[user_name]["password"]==pass_word:
        print("Login Successsfully")
        menu()
    else:
        print("Incorrect username or password")
        request=input("Do you want to change password?YES/NO?")
        if request =="YES":
            bank.changepassword()
        else:
            continue





























































































































































































