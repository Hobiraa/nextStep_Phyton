balance = 1000.00

print("Welcome to ATM")

while True :
     choice=input("Choose an option\n 1.Check Balance\n 2.Deposit\n 3.Withdrawn\n 4.Exit\n ")
    

if choice == "1":
            print(f"Your current balance is: {balance}")

elif choice =="2":
            amount = input("Enter deposit amount: ")
            
            balance = balance+int(amount)
            print("Your new balance is:" , balance)
elif choice == "3":
    
            amount = int(input("Enter withdrawal amount: "))
            if balance > amount:
                print("Not enough balance")
            else:
                print(f"{amount} is withdrawn from your account")
                balance = balance-amount
                print("Your current balance is ",balance)

elif choice =="4":
            print("Goodbye!")
else:
            print("Invalid choice. Please select a valid option.")
