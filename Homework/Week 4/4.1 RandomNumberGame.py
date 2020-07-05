from random import *

RandomInt=randint(1,15)
RemainingTries=5
print(RandomInt)
while RemainingTries>0:
    print("Remaining Tries: ", RemainingTries)
    Guess=int(input("Enter your guess: "))
    GuessDifference=abs(RandomInt-Guess)
    if Guess==RandomInt:
        print("You Win!!")
        quit()
    elif GuessDifference<3:
        print("Your Guess is close")
    RemainingTries-=1
if RemainingTries==0:
    print("You lost. The number was ", RandomInt)