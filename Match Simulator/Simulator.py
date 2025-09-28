import time
import random

batter= [ "Babar Azam","Rohit Sharma","Fakhar Zaman","Virat Kholi","David Warner","Ab Devilier","Brendon McCullum","Chris Gayle"]
pacer=  ["Shaheen Shah","Tim Southee","Kagiso Rabada","Lasit malinga","Mitchell Starc"]
spinner=["Nathon Lyon","Sajid Khan" ,"Shadab Khaan" , "Rashid Khan" ,"Adil Raashid",]
wk =    ["Mohammad Rizwan","MS Dhoni","Jos Buttler","Q De Kock"]

Squad1_names=[]
Squad2_names=[]

#Team Name Selection

Name1=input("Enter Player 1 Team Name |: ")
Name2=input("Enter Player 2 Team Name |: ")

#Selection Area
turn = 1
while turn < 3:    
    random.shuffle(batter)
    random.shuffle(pacer)
    random.shuffle(spinner)
    random.shuffle(wk)
    
    print("-----------------------------------------")
    print(f"Team {turn} Selection ")
    print("-----------------------------------------")
    for i in batter[:2]:
        print(f"| {i} " ,end=" | ")
    print()
    inp1 =input("Enter Your Selection :| ").lower()
    print("---------------------------------------------")
    if turn == 1:
      Squad1_names.append(inp1)   
    elif turn == 2:
       Squad2_names.append(inp1)   
    
    for i in batter[3:5]:
        print(f"{i}",end=" | ")
    print()
    inp2 =input("Enter Your Selection :| ").lower()
    print("---------------------------------------------")
    if turn == 1:
        Squad1_names.append(inp2)
    elif turn == 2:
        Squad2_names.append(inp2)     

    for i in wk[:2]:
         print(f"{i}",end=" | ")
    print()
    inp5 =input("Enter Your Selection :| ").lower()
    print("---------------------------------------------")
    if turn == 1:
        Squad1_names.append(inp5)
    elif turn == 2:
        Squad2_names.append(inp5)   

    for i in pacer[:2]:
      print(f"{i}",end=" | ")
    print()
    inp3 =input("Enter Your Selection :| ").lower()
    print("---------------------------------------------")
    if turn == 1:
        Squad1_names.append(inp3)
    elif turn == 2:
        Squad2_names.append(inp3)   

    for i in spinner[:2]:
        print(f"{i}",end=" | ")
    print()
    inp4 =input("Enter Your Selection :| ").lower()
    print("---------------------------------------------")
    if turn == 1:
        Squad1_names.append(inp4)
    elif turn == 2:
        Squad2_names.append(inp4)   

    turn +=1

#Squad Display
order1 = 1
print("="*45)
print(f" {Name1} Batting Order Is: ")
for i in Squad1_names:
   print(f"{order1}. {i}")
   order1 +=1

order2 = 1
print("="*45)
print(f" {Name2}  Batting Order Is: ")
for i in Squad2_names:
   print(f"{order2}. {i}")
   order2 +=1

#Match Simulator ------------- Commentry
print()
print("*******  Toss Time  ******** ")
print("-"*45)

batting_turn = 0

Toss_Result = random.randint(1,2)    
if Toss_Result == 1:
    print("Head Is the call !!!!!! ")
    time.sleep(2)
    print("and Head it is")
    Want_1 = input(f"{Name1}  Won The Toss And Elected To ").lower()
    
    if Want_1   == "batting":
        print(f"{Name1}  Decided To Bat First")
        batting_turn = 1
    elif Want_1 == "bowling":
        print(f"{Name1}  Decided To Bowl First")
        batting_turn = 2
        
elif  Toss_Result == 2:
    print("Head Is the call !!!!!! ")
    time.sleep(2)
    print("and Tail it is")
    Want_2 = input(f"{Name2} Won The Toss And Elected To ").lower()
     
    if Want_2   == "batting":
        print(f"{Name2}  Decided To Bat First")
        batting_turn = 2
    elif Want_2 == "bowling":
        print(f"{Name2}  Decided To Bowl First")
        batting_turn = 1

# Match Start
Inning_1 =0
Inning_2 =0 
wickets  =5

def Innings_Sim(Name,Squad_Turn):
 wickets  =5
 lineup   =0
 balls    =0
 score    =0

 for i in  range(12):
    runs = random.randint(0,7)
    if runs == 7 :
        score += 0
    else:
        score +=runs
        
    balls+= 1
    if   runs == 0:    
       print(f"Ball {balls}")
       time.sleep(1)
       print("-"*45)
       print("Play And Miss !!!! What A Peach of A delivery By The Bowler")
       print("="*45)
       time.sleep(4)
    
    elif runs == 1:  
        print(f"Ball {balls}")
        time.sleep(1)
        print("-"*45)
        print(f"{Squad_Turn[lineup]} Pushes The Ball Toward Legside For a Single ")
        print("="*45)
        time.sleep(4) 
    
    elif runs == 2:  
        print(f"Ball {balls}")
        time.sleep(1)
        print("-"*45)
        print(f"{Squad_Turn[lineup]} Pushes The Ball Into The Gap Toward offside For a Double !!!")
        print(f"Great Running by {Squad_Turn[lineup]} !!!")
        print("="*45)
        time.sleep(4)
    
    elif runs == 3:  
        print(f"Ball {balls}")
        time.sleep(1)
        print("-"*45)
        print(f"{Squad_Turn[lineup]} Plays A Beautiful Shot Toward Legside But Wait !!!")
        time.sleep(2)
        print(f"That was Stop By the Fielder ...... He was Runnintg like bullet !!!")
        print(f"{Squad_Turn[lineup]} Gets 3 Runs Of this shot ")
        print("="*45)
        time.sleep(4)
    
    elif runs == 4:  
        print(f"Ball {balls}")
        time.sleep(1)
        print("-"*45)
        print(f"{Squad_Turn[lineup]} Wohooo !!!  What a Brilliant Shot straight Down the Ground ")
        print( "For Four Runs  That Was Such A treat To Watch ")
        print("="*45)
        time.sleep(4)
    
    elif runs == 5:  
        print(f"Ball {balls}")
        time.sleep(1)
        print("-"*45)
        print(f"{Squad_Turn[lineup]} ohooo !!! That Was a hurendous Mistake By Keeper  ")
        print( "That Cost The Fielding team ..... Whooping 5 Runs ")
        print("="*45)
        time.sleep(4)
    
    elif runs == 6:  
        print(f"Ball {balls}")
        time.sleep(1)
        print("-"*45)
        print(f"{Squad_Turn[lineup]} Bang !!! Out Of The Ground For A Six Runs ")
        print(f"{Squad_Turn[lineup]} Played Shot of The Day")
        print("="*45)
        time.sleep(4)
    
    elif runs == 7:
        print(f"Ball {balls}")
        time.sleep(1)
        print("-"*45)
        print(f"{Squad_Turn[lineup]} Gets out ") 
        print("="*45)
        time.sleep(4)
        lineup +=1
        wickets -=1
        if lineup >= len(Squad_Turn):
            print(f"That End up Here For As {Name} Gets Allout ")
            print(f"{Squad_Turn[4]} Gets Out")
            break
        else :
            print(f"{Squad_Turn[lineup]} Comming Up onto the Crease !!!!") 
            print("="*45)
            time.sleep(4)
# Inning Break
    print("-"*45) 
    print(f" | {runs} | Runs ")
    print("-"*45)
    print(f"{Name} | {score}/{lineup} In {balls} Balls ")
    print()
 return score   

if batting_turn == 1: 
    Inning_1 = Innings_Sim(Name1,Squad1_names)  
    wickets  =5
    Inning_2 = Innings_Sim(Name2,Squad2_names)  
   
    Margin1=Inning_1-Inning_2
    Margin2=Inning_2-Inning_1

    if Inning_1>Inning_2:
        print(f"{Name1} Won by {Margin1} Runs")
    elif Inning_2>Inning_1:
        print(f"{Name2} Won By {wickets} Wickets")

elif batting_turn == 2:    
    Inning_2 = Innings_Sim(Name2,Squad2_names)  
    wickets  =5
    Inning_1 = Innings_Sim(Name1,Squad1_names)

    Margin1=Inning_1-Inning_2
    Margin2=Inning_2-Inning_1

    if Inning_2>Inning_1:
        print(f"{Name2} Won by {Margin2} Runs")
    elif Inning_1>Inning_2:
        print(f"{Name1} Won By {wickets} Wickets")

