import os
import time

print       ("---------------------------------------")
print       ("  Welcome To A 2-Player HangMan Game   ")
print       ("---------------------------------------")
name1= input("Player One Name |: ")
name2= input("Player Two Name |: ")

while True:
 def Player1():  
  inp1  =input(f"  {name1} Select Your Player  |:").lower()
  print       ("---------------------------------------")
  role  =input("  Your Player Role   : ")
  nation=input("  Your Player Nation : ") 
  hand  =input("  Your Player Prefered Hand : ")
  print("--------------------------------------------------")
  
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear') 
              
  def hint():
    print(f" {name1} Cricketer Name Has {len(inp1)} Letters ")
    print(f" {name1} Cricketer Is Playing For {nation} and Playing As a {hand}-{role}.")
    print("---------------------------------------------------------------------------")
     
  hint()
  guess =input(f"{name2} Guess |: ").lower()
  print("--------------------------------------------------")
  
  if guess == inp1 :
      print("Correct Answer !!!! ")
      print() 
  else :
     print("Ohoo !!!  Wrong Answer.")
     hint()  
     guess1 =input(f" {name2} Guess |: ").lower()

     if guess1 == inp1 :
        print("Correct Answer !!!! ")
     else :
        print("Ohoo !!!  Wrong Answer.")
        print(f"Correct Answer Was {inp1}")
 Player1()
 
 print("---------------------------------------------------")
 print(f"Now {name2} Turn To Give The Cricketer To Guess")        
 print("---------------------------------------------------")

 def Player2():  
  inp1  =input(f"  {name2} Select Your Player  |:").lower()
  print       ("---------------------------------------")
  role  =input("  Your Player Role   : ")
  nation=input("  Your Player Nation : ") 
  hand  =input("  Your Player Prefered Hand : ")  

  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear') 
  # inputs.append(inp1)            
  def hint():
    print(f" {name2} Cricketer Name Has {len(inp1)} Letters ")
    print(f" {name2} Cricketer Is Playing For {nation} and Playing As a {hand}-{role}.")
 
  hint()
  guess1 =input(f"{name1} Guess |: ").lower()
  
  if guess1 == inp1 :
      print("Correct Answer !!!! ")
  else :
     print("Ohoo !!!  Wrong Answer.")
     hint()  
     guess1 =input(f"{name1} Guess |: ").lower()

     if guess1 == inp1 :
        print("Correct Answer !!!! ")
     else :
        print("Ohoo !!!  Wrong Answer.")
        print(f"Correct Answer Was {inp1}")
 Player2()

 print("-------------------------------------------------------")
 print("         | Do You Want To Play Again |")
 i=input("| Press Any Key To Continue ........ Press 'X' To Exit |")

 if i == "X" or i == "x":
    break
 else:
     os.system('cls' if os.name == 'nt' else 'clear')