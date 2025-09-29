import time
import os
import random

class batsmen :
   def __init__(self,name,sr,run,sixes,four):
    self.name    =name
    self.sr      = sr
    self.run     = run
    self.sixes   = sixes
    self.four    = four

class bowler :
   def __init__(self,name,average,wickets,economy):
    self.name=name
    self.average = average
    self.wickets = wickets
    self.economy = economy

class keeper :
   def __init__(self,name,catches,stumping,):
    self.name=name   
    self.catches = catches
    self.stumping = stumping
   
#batter                                SR | Runs | Six | Fours
babar    =batsmen("Babar Azam"       , 129 , 4223 , 73  , 447)
rohit    =batsmen("Rohit Sharma"     , 141 , 4231 , 205 , 383)
fakhar   =batsmen("Fakhar Zaman"     , 133 , 1849	, 78  , 172)
virat    =batsmen("Virat Kholi"      , 137 , 4188 , 124 , 369)
warner   =batsmen("David Warner"     , 142 , 3277 , 122 , 338)
buttler  =batsmen("Jos Buttler"      , 147 , 3700 , 160 , 333)
pooran   =batsmen("Nicholes Pooran"  , 136 , 2275 , 149 , 152)   
abd      =batsmen("Ab Devilier"      , 141 , 2552 , 128 , 166)
guptil   =batsmen("Martin Guptill"   , 136 , 3531 , 173 , 310)
#pacer                              Avg | Wick | Economy
shaheen  = bowler("Shaheen Shah"   , 22 , 102 , 7   )
southe   = bowler("Tim Southee"    , 22 , 164 , 6   )
arshdeep = bowler("Arshdeep"       , 18 , 99  , 7   )
rabada   = bowler("Kagiso Rabada"  , 27 , 71  , 8   )
malinga  = bowler("Lasit malinga"  , 21 , 107 , 7   )
hassan   = bowler("Hassan Ali"     , 23 , 60  , 7.5 )
#spinner
zampa     = bowler("Adam Zampa"     , 21 , 117 , 6 )
shamsi    = bowler("Tabraiz Shamsi" , 21 , 89  , 6 )
shadab    = bowler("Shadab Khaan"   , 14 , 159 , 7 )
rashid    = bowler("Rashid Khan"    , 21 , 65  , 6 )
adil      = bowler("Adil Raashid"   , 24 , 135 , 7 )
hasaranga = bowler("Hasaranga"       , 15 , 131 , 7 )
#keeper                           catch | stump
rizwan   = keeper("Mohammad Rizwan" , 41 , 11 )
dhoni    = keeper("MS Dhoni"        , 57 , 34 )
ramdin   = keeper("Danesh Ramdin"   , 43 , 20 )
dekock   = keeper("Q De Kock"       , 84 , 18 )
rahim    = keeper("Mushfiqur Rahim" , 32  , 30)

pool=[ babar,rohit,fakhar,virat,warner,abd,guptil,pooran,buttler,
      southe,shaheen,arshdeep,rabada,malinga,hassan,
      zampa,shamsi,shadab,adil,rashid,hasaranga,
      rizwan,dhoni,ramdin,dekock,rahim]

#For Player1
Sr    =[]
Run    =[]
Six    =[]
Four   =[]
Wicket =[]
Avg    =[]
Eco    =[]
Catch  =[]
Stump  =[]
#For Player2
Sr1     =[]
Run1    =[]
Six1    =[]
Four1   =[]
Wicket1 =[]
Avg1    =[]
Eco1    =[]
Catch1  =[]
Stump1  =[]

batter= [ babar.name , rohit.name , fakhar.name ,virat.name ,warner.name , abd.name, guptil.name, pooran.name, buttler.name]
pacer=  [ southe.name ,shaheen.name ,arshdeep.name ,rabada.name ,malinga.name ,hassan.name]
spinner=[ zampa.name ,shamsi.name ,shadab.name ,adil.name ,rashid.name ,hasaranga.name ]
wk =    [ rizwan.name ,dhoni.name ,ramdin.name ,dekock.name ,rahim.name ]

selected=[]
selected1=[]
item=[]
item1=[]

def player1():
 random.shuffle(batter)
 #ROUND 1 
 print("Round 1: Batter ")
 print("---------------------------------------------")
 for i in batter[:2]:
  print(f"{i}",end=" | ")
 print()
 print("---------------------------------------------")
 inp = input("Your Selection (last Name) :").lower() 
 #ROUND 2 
 print("Round 2: Batter ")
 print("--------------------------------------------")
 for i in batter[3:5]:
  print(f"{i}",end=" | ")
 print()
 print("---------------------------------------------")
 inp1 = input("Your Selection (last Name) :").lower()   
 #ROUND 3
 random.shuffle(wk)
 print("Round 3: Wicket Keeper ")
 print("---------------------------------------------")
 for i in wk[:2]:
  print(f"{i}",end=" | ")
 print()
 print("---------------------------------------------")
 inp2 = input("Your Selection (last Name) :").lower() 
 #ROUND 4
 random.shuffle(spinner)
 print("Round 4: Spinner ")
 print("---------------------------------------------")
 for i in spinner[:2]:
   print(f"{i}",end=" | ")
 print()
 print("---------------------------------------------")
 inp3 = input("Your Selection (last Name) :").lower()  
 #ROUND 5
 random.shuffle(pacer)
 print("Round 5: pacer ")
 print("---------------------------------------------")
 for i in pacer[:2]:
   print(f"{i}",end=" | ") 
 print()
 print("---------------------------------------------")
 inp4 = input("Your Selection (last Name) :").lower()  

 squad1=[inp,inp1,inp2,inp3,inp4]
 print("---------------------------------------------------------")
 print(f"Your Squad : {inp} | {inp1} | {inp2} | {inp3} | {inp4} |") 
 print("---------------------------------------------------------")
 print("| Now There will be 5 Seconds To see Your Players stats |")
 for player1 in pool:
    Name = player1.name.lower().split() # get last name
    for Inp in squad1:
          if Inp.lower() in Name:
            print("-------------------------------------------------------------------")
            print(f"--- Stats for {player1.name} ---")
            print("-------------------------------------------------------------------")
            if isinstance(player1, batsmen):
                print(f"Runs : {player1.run} | SR  : {player1.sr} | 6s : {player1.sixes}  | 4s : {player1.four}")
                
            elif isinstance(player1, bowler):
                print(f"Wickets : {player1.wickets} | Avg : {player1.average} | Econ : {player1.economy} |")

            elif isinstance(player1, keeper):
                print(f"Catches  : {player1.catches} | Stumpings: {player1.stumping}")                
            selected.append(player1)
 time.sleep(5)  
 os.system('cls' if os.name == 'nt' else 'clear')  
 print("Time's up! Get ready to face Player2 !\n")
def player2():
 random.shuffle(batter)
 #ROUND 1 
 print("Round 1: Batter ")
 print("---------------------------------------------")
 for i in batter[:2]:
  print(f"{i}",end=" | ")
 print()
 print("---------------------------------------------")
 inp = input("Your Selection (last Name) :").lower() 
 #ROUND 2 
 print("Round 2: Batter ")
 print("--------------------------------------------")
 for i in batter[3:5]:
  print(f"{i}",end=" | ")
 print()
 print("---------------------------------------------")
 inp1 = input("Your Selection (last Name) :").lower()   
 #ROUND 3
 random.shuffle(wk)
 print("Round 3: Wicket Keeper ")
 print("---------------------------------------------")
 for i in wk[:2]:
  print(f"{i}",end=" | ")
 print()
 print("---------------------------------------------")
 inp2 = input("Your Selection (last Name) :").lower() 
 #ROUND 4
 random.shuffle(spinner)
 print("Round 4: Spinner ")
 print("---------------------------------------------")
 for i in spinner[:2]:
   print(f"{i}",end=" | ")
 print()
 print("---------------------------------------------")
 inp3 = input("Your Selection (last Name) :").lower()  
 #ROUND 5
 random.shuffle(pacer)
 print("Round 5: pacer ")
 print("---------------------------------------------")
 for i in pacer[:2]:
   print(f"{i}",end=" | ") 
 print()
 print("---------------------------------------------")
 inp4 = input("Your Selection (last Name) :").lower()  

 squad2=[inp,inp1,inp2,inp3,inp4]

 print("---------------------------------------------------------")
 print(f"Your Squad : {inp} | {inp1} | {inp2} | {inp3} | {inp4} |") 
 print("---------------------------------------------------------")
 print("| Now There will be 5 Seconds To see Your Players stats |")
 for player2 in pool:
    Name = player2.name.lower().split() # get last name
    for Inp in squad2:
          if Inp.lower() in Name:
            print("-------------------------------------------------------------------")
            print(f"--- Stats for {player2.name} ---")
            print("-------------------------------------------------------------------")
            if isinstance(player2, batsmen):
                print(f"Runs : {player2.run} | SR  : {player2.sr} | 6s : {player2.sixes}  | 4s : {player2.four}")
                
            elif isinstance(player2, bowler):
                print(f"Wickets : {player2.wickets} | Avg : {player2.average} | Econ : {player2.economy} |")

            elif isinstance(player2, keeper):
                print(f"Catches  : {player2.catches} | Stumpings: {player2.stumping}")                
            selected1.append(player2)
 time.sleep(5)  
 os.system('cls' if os.name == 'nt' else 'clear')  
 print("Time's up! Get ready to face Player2 !\n")

player1()
player2()
  
print("---------------------------------------------")
print("|     Select the option To compare          |")
print("---------------------------------------------")

for player in selected:
  if isinstance(player,batsmen):
    print(f"{player.name} : | Strike Rate  | Runs | Sixes | Fours |")
    sel = input("Your selection : ").lower()
    if sel == "sr":
      item.append(player.sr)
      Sr.append(player.sr)  
    elif sel == "runs":
      item.append(player.run)
      Run.append(player.run)  
    elif sel == "sixes":
      Six.append(player.sixes)  
      item.append(player.sixes)     
    elif sel == "fours":
      item.append(player.four)
      Four.append(player.four)  

  elif isinstance(player,bowler):
    print(f"{player.name} : | wickets  | average | economy |")
    sel = input("Your selection : ").lower()
    if sel == "wickets":
       item.append(player.wickets)
       Wicket.append(player.wickets)  
    elif sel == "average":  
      Avg.append(player.average)  
      item.append(player.average)
    elif sel == "economy":
      item.append(player.economy)
      Eco.append(player.economy)  
    
  elif isinstance(player,keeper):
    print(f"{player.name} : | stumping | catches |")
    sel = input("Your selection : ").lower()
    if sel == "stumping":
      item.append(player.stumping)
      Stump.append(player.stumping)  
    elif sel == "catches":
      item.append(player.catches)  
      Catch.append(player.catches) 
time.sleep(4)
print()

for player in selected1:
   if isinstance(player,batsmen):
    print(f"{player.name} : | Strike Rate  | Runs | Sixes | Fours |")
    sel1 = input("Your selection : ").lower()
    if sel1 == "sr":
      item1.append(player.sr)
      Sr1.append(player.sr)        
    elif sel1 == "runs":
      item1.append(player.run)
      Run1.append(player.run)  
    elif sel1 == "sixes":
      Six1.append(player.sixes)  
      item1.append(player.sixes)     
    elif sel1 == "fours":
      item1.append(player.four)
      Four1.append(player.four)  
      
   elif isinstance(player,bowler):
    print(f"{player.name} : | wickets  | average | economy |")
    sel1 = input("Your selection : ").lower()
    if sel1 == "wickets":
       item1.append(player.wickets)
       Wicket1.append(player.wickets)  
    elif sel1 == "average":
      item1.append(player.average)
      Avg1.append(player.average)  
    elif sel1 == "economy":
      item1.append(player.economy)  
      Eco1.append(player.economy)     
    
   elif isinstance(player,keeper):
    print(f"{player.name} : | stumping | catches |")
    sel1 = input("Your selection : ").lower()
    if sel1 == "stumping":
       Stump1.append(player.stumping) 
       item1.append(player.stumping)
    elif sel1 == "catches":
      item1.append(player.catches)
      Catch1.append(player.catches) 
time.sleep(4)
print()

score1=[]
score2=[]

print(item)
print(item1)
#---------------------------------------|Point System|-----------------------------------
#player1
for a in item :
  #------------------------------------| batting |---------------------------------------------
  if a in Sr:
    if a>130 :
      s = a*3
    else:  
      s= a*2
    score1.append(s) 
  elif  a in Run:
    r = a/2
    score1.append(r)
  elif a in Six:
    if a>70 and a<=95:
      si = a*3
    elif a>96 and a<=130:  
      si= a*4
    elif a>131:
      si= a*5
    else:
      si= a*2 
    score1.append(si)  
  elif a in Four:
    if a>80 and a<=95:
       f = a*3
    elif a>96 and a<=115:  
       f= a*4
    elif a>116:
       f =a*5
    else :
       f=a*2  
    score1.append(f)        
  #---------------------------| bowling |------------------------
  elif a in Eco:
    if a == 8 :
      e = 200
    elif a == 7:
      e = 300
    else:
      e = 400       
    score1.append(e) 
  elif a in Wicket:
    if a>69 and a<=80:
      w = a*2
    elif a>81 and a<=100:  
      w= a*3
    else:
      w= a*4 
    score1.append(w)  
  elif a in Avg:
    if a>19 and a<=22:
       av = 200
    else :
      av =400 
    score1.append(av)
      #---------------------------------| keeping |-------------------------------------
  elif a in Stump:
     st = a*4     
     score1.append(st) 
  elif a in Catch:
     c = a*2
     score1.append(c)
#player2
for b in item1 :
  #------------------------------------| batting |---------------------------------------------
  if b in Sr1:
    if b>120:
      s1 = b*3
    else :  
      s1= b*2
    score2.append(s1) 
  elif  b in Run1:
    r1 = b/2
    score2.append(r1)
  elif b in Six1:
    if a>70 and a<=95:
      si1 = a*3
    elif a>96 and a<=130:  
      si1= a*4
    elif a>131:
      si1= a*5
    else:
      si1= a*2 
    score2.append(si1)  
  elif b in Four1:
     if a>80 and a<=95:
       f1 = a*3
     elif a>96 and a<=115:  
       f1= a*4
     elif a>116:
       f1 =a*5
     else :
       f1=a*2  
     score2.append(f1)        
  #---------------------------| bowling |------------------------
  elif b in Eco1:
    if b == 8 :
      e1 = 200
    elif b == 7:
      e1 = 300
    else :
      e1 = 400       
    score2.append(e1) 
  elif b in Wicket1:
    if a>69 and a<=80:
      w1 = a*2
    elif a>81 and a<=100:  
      w1= a*3
    else:
      w1= a*4 
    score1.append(w)  
    score2.append(w1)  
  elif b in Avg1:
    if a>19 and a<=22:
       av1 = 200
    else :
      av1 =400 
    score2.append(av1)
  #---------------------------------| keeping |-------------------------------------
  elif b in Stump1:
     st1 = b*4     
     score2.append(st1) 
  elif b in Catch1:
     c1 = b*2
     score2.append(c1)


play1 = sum(score1)
play2 = sum(score2)

print(score1)
print(score2)

time.sleep(5)

print(play1)
print(play2)

if play1>play2 :
   print("---------------------------------------------")
   print(f"Player One Score : {play1}")
   print("---------------------------------------------")
   time.sleep(3)
   print(f"Player Two Score : {play2}")
   print("---------------------------------------------")
   print("Player One Is the Winner ")
elif play2>play1 :
   print("---------------------------------------------")
   print(f"Player One Score : {play1}")
   print("---------------------------------------------")
   time.sleep(3)
   print(f"Player Two Score : {play2}")
   print("---------------------------------------------")
   print("Player Two Is the Winner ")   

time.sleep(10)   