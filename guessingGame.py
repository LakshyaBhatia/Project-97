import random 
computer = random.randint(1,9)
chance = 5
x=int(input("enter the no. which you think computer generated"))
while(chance>1):
    chance = chance-1
    if x== computer:
        print("correct guess")
        break
    else :
        x = int(input("guess again"))
        print("better luck next time")
    