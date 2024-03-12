import random

minNum = input("Enter the minimam number: ")
maxNum = input("Enter maximam number: ")

correctAnswer = random.randint(int(minNum), int(maxNum))

n = 5
while(n > 0):
    print("guess the answer within " + str(n))
    guessNumber = input("Guess the random number: ")
    if(int(guessNumber) == correctAnswer):
        print("That's correct!")
        break
    else:
        print("That's wrong...")
        n -=1

if(n == 0):
    print("You couldn't guess the answer... Please continue")