import random
random_number = random.randint(1, 100)
Guess = input("please Enter a random number between 1 and 100: ")
if int(Guess) == random_number:
    print("Congratulations! you got the right nmumber")
    elif int(Guess