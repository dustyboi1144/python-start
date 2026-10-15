print("scissor paper rock")
handsign=input("enter the handsign (rock/paper/scissor):").lower()
choices=["rock","paper","scissor"]
import random
computer=random.choice(choices)
print("computer chose:",computer)
if handsign == computer:
    print("draw!")
elif ((handsign == "rock" and computer=="scissor") or 
      (handsign=="paper" and computer=="rock") or 
      (handsign=="scissor" and computer=="paper")):
      print("you win!")
else:
    print("you lose!")


