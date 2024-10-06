#Snake,water and gun game
'''
1 for snake
-1 for water
0 for gun
'''

import random

computer=random.choice([-1,0,1])
youstr=input("Enter your choice: ")

youDict={"s": 1, "w": -1, "g": 0}
reversedDict={1: "snake", -1: "water", 0: "gun"}
you =youDict[youstr]

#by now we have 2 numbers(variables) , you and computer

print(f"you chose: {reversedDict[you]}\ncomputer choose: {reversedDict[computer]}")
if(computer==you):
  print("its draw! ")
  
else:  
  if(computer == -1 and you==1):
    print("You win: ")

  elif(computer==-1 and you==0):
    print("You lose: ")  
    
  elif(computer==1 and you==-1):
    print("you lose! ")
    
  elif(compile==1 and you==0):
    print("you win! ")    
    
  elif(computer==0 and you==1):
    print("you lose! " )  
    
  else:
    print("something went wrong: ")  
 
    
    
 #second way when analyse the game
'''
import random

computer=random.choice([-1,0,1])
youstr=input("Enter your choice: ")

youDict={"s": 1, "w": -1, "g": 0}
reversedDict={1: "snake", -1: "water", 0: "gun"}
you =youDict[youstr]

#by now we have 2 numbers(variables) , you and computer

print(f"you chose: {reversedDict[you]}\ncomputer choose: {reversedDict[computer]}")   

if((computer - you) == -1) or (computer - you ==2)):
  print("You lose! ")
  
else:
  print("You win!")  
'''