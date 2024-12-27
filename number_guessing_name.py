import random

number = random.randint(1, 10)
attempt=0

while attempt <= 3:
        user_guess = int(input("guess any number betwenn 1-10"))
        attempt +=1
        if user_guess>10 and user_guess<0:
             print("Enter valid number")
        else:

          if number == user_guess:
             print ("Congrats !!!!!!!!!")
             break
          elif user_guess < number:
             print("your guess is low, guess higher number")
          else:
             print("Your guess is high, guess lower number")


