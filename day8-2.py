#Maurel ZODOGANHOU
#DAY_8-DJANGO-CHALLENGE
#ROCK, PAPER, SCISSORS GAME
import random

def main():
    print("Possible options are:")
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
    print()
  
    status=True
    while status == True:
    # generate random number
        ran_num = RandomNumberGenerator()
        user_choice = int(input("Please enter your choice as number: "))
        print()
        ShowComputerChoice(ran_num)
        ShowUserChoice(user_choice)
        status = DetermineWinner(ran_num, user_choice)
    
def RandomNumberGenerator():
    ran_num = random.randint(1,3)
    return ran_num

def ShowComputerChoice(ran_num):
    if ran_num == 1:
        print("Computer chose rock.")
    elif ran_num == 2:
        print("Computer chose paper.")
    else:
        print("Computer chose scissors.")
        
def ShowUserChoice(user_choice):
    if user_choice == 1:
        print("You chose rock.")
    elif user_choice == 2:
        print("You chose paper.")
    else:
        print("You chose scissors.")
        
def DetermineWinner(ran_num, user_choice):
    print()
    status = False
    if ran_num == 1 and user_choice == 3:
        print("You lost. Rock smashes scissors.")
    elif ran_num == 3 and user_choice == 1:
        print("You won. Rock smashes scissors.")
    elif ran_num == 1 and user_choice == 2:
        print("You won. Paper wraps rock.")
    elif ran_num == 2 and user_choice == 1:
        print("You lost. Paper wraps rock")
    elif ran_num == 2 and user_choice == 3:
        print("You won. Scissors cuts paper.")
    elif ran_num == 3 and user_choice == 2:
        print("You lost. Scissors cuts paper.")
    elif ran_num == user_choice:
        print("*****It is a draw try again*****")
        status = True     
    return status

main()
    
        
    