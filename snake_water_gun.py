import random

computer = random.choice([-1,0,1])
mychoice = input("Choose Your Choice [s for Snake, w for Water & g for Gun]: ").lower()
gamechoices = {"s" : 1, "w" : -1, "g" : 0}
reversedgamechoices = {1 : "Snake", -1 : "Water", 0 : "Gun"}

you = gamechoices[mychoice]

print(f"You Choose: {reversedgamechoices[you]}  \nComputer Choose: {reversedgamechoices[computer]}")

if(computer == you):
    print("The Game is Tie!")

elif(computer == 1 and you == -1):
    print("You Lose!")

elif(computer == 1 and you == 0):
    print("You Win!")

elif(computer == -1 and you == 1):
    print("You Win!")

elif(computer == -1 and you == 0):
    print("You Lose!")

elif(computer == 0 and you == 1):
    print("You Lose!")

elif(computer == 0 and you == -1):
    print("You Win!")

else:
    print("Something Went Wrong")


# Short Maths Based Concept Instead Of Elif Chain
    ''' if((computer - you) == -1 or (computer - you) == 2):
        print("You lose!")
    else:
        print("You Win!") '''