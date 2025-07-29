dictionary = {

    "current_balance" : 0

}

def menu():

    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Exit the program")
    
def deposit(current_balance, deposit_amount):
    
    new_balance = dictionary["current_balance"] + deposit_amount

    return new_balance

def withdraw(money):

    if money <= dictionary["current_balance"]:

        new_balance = dictionary["current_balance"] - money

        return new_balance
    
def check_balance():
    return dictionary["current_balance"]


print("Welcome to Bank Account Simulator!")

option = 0

while option != 4:

    menu()

    option = int(input("Choose an option (1, 2, 3, 4): "))


    if option == 1:


        deposit_amount = float(input("Please enter deposit amount: $"))

        new_balance = deposit(dictionary["current_balance"], deposit_amount)

        print(f"New balance: ${new_balance:.2f}")

        dictionary["current_balance"] = new_balance

        
    elif option == 2:

        money = float(input("Enter money for withdraw: $"))

        if withdraw(money) == None:

            print("Sorry, you are broke!")

        else:

            new_balance = withdraw(money)

            print(f"New balance: ${new_balance:.2f}")

            dictionary["current_balance"] = new_balance

    elif option == 3:
    
        print(f"Current Balance: {check_balance():.2f}")

else:

    print("Goodbye!")



        
        



        


