import random as rd
option=["rock", "paper" , "scissor"]
for i in range(0,3):
    player= input("Choose rock, paper, scissor: ")
    computer=rd.choice(option)
    print(computer)
    if player==computer:
        print("Draw")
        break
    elif player == "rock" and computer =="paper":
         print("Computer win")
    elif player=="rock" and computer=="scissor":
        print("Player wins")
    elif player=="paper" and computer=="rock":
        print("Player wins")
    elif player=="paper" and computer=="scissor":
        print("Computer wins")
    elif player=="scissor" and computer=="rock":
        print("Player wins")
    elif player=="scissor" and computer=="paper":
        print("Computer win")
    else:
        print("Enter correct value")