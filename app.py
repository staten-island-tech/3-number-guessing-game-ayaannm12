import random
random_number = random.randint(1, 100)
validNumber = False
solved = False
while solved == False:
    while validNumber == False:
        Guess = input("please Enter a random number between 1 and 100: ")
        if not input == int:
                print("Please enter a valid number")
        else:
            validNumber = True
    if int(Guess) == random_number:
        print("Congratulations! you got the right nmumber")
        solved = True
    elif int(Guess) < random_number:
        print("Your Guess is too Low")
    else:
        print("Your guess is too High")