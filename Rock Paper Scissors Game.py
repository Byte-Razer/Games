import random
print("Welcome to Rock🪨, Paper📄 Scissors✂️")
options=["rock","paper","scissors"]
continuechoice="yes"
while continuechoice=="yes" or continuechoice=="y":
    print("")
    computerchoice=random.choice(options)
    userchoice=input("Rock, Paper or Scissors:\n").lower().strip()
    while userchoice!="rock" and userchoice!="scissors" and userchoice!="paper":
        print("Invalid")
        userchoice=input("Rock, Paper or Scissors:\n").lower().strip()
    print(f"The Computer has played {computerchoice}") 
    if userchoice==computerchoice:
        print("Tie")
    if computerchoice=="rock":
        if userchoice=="paper":
            print("You win :)")
        elif userchoice=="scissors":
            print("You lost :(")
    elif computerchoice=="scissors":
        if userchoice=="rock":
            print("You win :)")
        elif userchoice=="paper":
            print("You lose :(")
    else:
        if userchoice=="scissors":
            print("You won :)")
        elif userchoice=="rock":
            print("You lose :(")
    continuechoice=input("Do you wish to continue?\nYes or No.  ").lower().strip()
print("Hope you enjoyed!😊")


