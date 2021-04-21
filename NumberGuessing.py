number = 5
guess = int(input("Guess a number from 1 to 9:  "))
if(guess>number):
    print("Wrong! A bit too high")
    guess = int(input("Guess a number from 1 to 9:  "))
    if(guess>number):
        print("Wrong! A bit too high")
        guess = int(input("Guess a number from 1 to 9:  "))
    elif(guess<number):
        print("Wrong! A bit too low")
        guess = int(input("Guess a number from 1 to 9:  "))
    elif(guess==number):
        print("Congratulations! You guessed it!")
elif(guess<number):
    print("Wrong! A bit too low")
    guess = int(input("Guess a number from 1 to 9:  "))
    elif(guess==number):
        print("Congratulations! You guessed it!")
elif(guess==number):
        print("Congratulations! You guessed it!")