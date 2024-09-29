# PROGRAM TITLE: THE NUMBER GUESSING GAME
# STUDENT: MAX DE JANON
# SECTION: 15889
# DATE: 2/29/2024

# Imports random module to generate a random number for the guessing game.
import random
answer = random.randint(1,100)
print('I am picking a number between 1 and 100.')
#print(answer)  #Remove # to display the randonm number to testing/debuggin.


# Variables for an attempt counter and the last number picked.
counter = 1
lastPick = 0


# Ask the user to enter a number and saves his input number if it is withing the game paramenters.
userInput = int(input('Guess the number I picked: '))
if userInput >= 1 and userInput <= 100:
    lastPick = userInput
    #print(lastPick) #Remove # to display the last number picked that is withing the games parameters for testing/debugging.


# While loop that compares the users number to the random number that the program generated.
while True:
    if userInput == answer or userInput == -99:
        #print(counter)     #Remove # to display the count for testing/debugging.
        break
    elif userInput <= 0 or userInput >= 101:
        userInput = int(input(f'Your number {userInput} is not between 1 and 100. Try again or enter -99 to stop: '))
        #print(counter)     #Remove # to display the count for testing/debugging.
    else:
        if userInput > answer and userInput <=100:
            userInput = int(input('Your number is greater then my number. Try again or enter -99 to stop: '))
            if userInput != -99:
                counter = counter + 1
                if userInput >=1 and userInput <= 100:
                    lastPick = userInput
            #print(counter)     #Remove # to display the count for testing/debugging.
            #print(lastPick) #Remove # to display the last number picked that is withing the games parameters for testing/debuggi
        else:
            userInput = int(input('Your number is smaller then my number. Try again or enter -99 to stop: '))
            if userInput != -99:
                counter = counter + 1
                if userInput >=1 and userInput <= 100:
                    lastPick = userInput                
            #print(counter)     #Remove # to display the count for testing/debugging.
            #print(lastPick) #Remove # to display the last number picked that is withing the games parameters for testing/debuggi

if userInput == answer:
    if counter == 1:
        print(f"My number was {answer} and you picked {userInput}. You guessed it on your first try! You are Awesome.")
    elif counter >=2 and counter <= 5:
        print(f"My number was {answer} and you picked {userInput}. It took you {counter} (correct) tries. Good Job!")
    elif counter >=6 and counter <= 10:
        print(f"My number was {answer} and you picked {userInput}. It took you {counter} (correct) tries. You need more practice.")
    else:
        print(f"My number was {answer} and you picked {userInput}. It took you {counter} (correct) tries. Don't play the lottery.")
else:
    if lastPick == 0:
        print(f"Hope you come back.")
    elif answer > lastPick:
        difference = answer - lastPick
        print(f"You were {difference} away from my number and you tried {counter} times. Better luck next time.")
    else:
        difference = lastPick - answer
        print(f"You were {difference} away from my number and you tried {counter} times. Better luck next time.")
