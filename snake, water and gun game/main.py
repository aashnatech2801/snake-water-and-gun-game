import random

'''
1 for snake
-1 for water
0 for gun
Rules:
- both choose same = tie
- water vs snave = snake wins
- water vs gun = water wins
- snake vs gun = gun wins
'''

computer= random.choice([0,1,-1]) 
youstr =  input("Enter your choice (snake, water, gun): ")
youDict = {"snake": 1, "water": -1, "gun": 0}
reverseYouDict = {1: "snake", -1: "water", 0: "gun"}
you = youDict[youstr]
#by now we have two numbers(computer and you)

print(f"Computer chose {reverseYouDict[computer]} \n You chose {reverseYouDict[you]}") 
#this is to print what computer and you chose in words instead of numbers 

if (computer == you):
    print("It's a tie")
#checking for tie condition


else:
    if (computer ==-1 and you== 1):
        print("You win") # snake wins over water
    elif (computer == -1 and you == 0):
        print("Computer wins") # water wins over gun
    elif (computer == 1 and you == -1):
        print("Computer wins") # snake wins over water
    elif (computer == 1 and you == 0):
        print("You win") # gun wins over snake  
    elif (computer == 0 and you == -1):
        print("You win") # water wins over gun
    elif (computer == 0 and you == 1):
        print("Computer wins") # gun wins over snake
    else:
        print("something went wrong")
#comparing the two numbers according to the rules and printing the result 




'''short version of the above code
(THE BELOW LOGIC IS WRITTEN ON THE BASIS OF COMPUTER'S CHOICE - USER'S CHOICE)


if (computer == you):
    print("It's a tie")
else:
    if ((computer - you) ==-1 or (computer - you) == 2):
        print("Computer wins")
    else:
        print("You win")
'''