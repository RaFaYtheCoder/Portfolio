import time
import random
import datetime

class batsmen:
    def __init__(self, name, run, sixes, four):
        self.name = name
        self.run = run
        self.sixes = sixes
        self.four = four

    def __str__(self):
        return self.name

class bowler:
    def __init__(self, name, average, wickets):
        self.name = name
        self.average = average
        self.wickets = wickets

    def __str__(self):
        return self.name

class keeper:
    def __init__(self, name, catches, stumping):
        self.name = name
        self.catches = catches
        self.stumping = stumping

    def __str__(self):
        return self.name

# Players
babar = batsmen("Babar Azam", 4223, 73, 447)
rohit = batsmen("Rohit Sharma", 4231, 205, 383)
fakhar = batsmen("Fakhar Zaman", 1849, 78, 172)
virat = batsmen("Virat Kohli", 4188, 124, 369)
warner = batsmen("David Warner", 3277, 122, 338)
buttler = batsmen("Jos Buttler", 3700, 160, 333)
pooran = batsmen("Nicholas Pooran", 2275, 149, 152)
abd = batsmen("AB de Villiers", 2552, 128, 166)
guptil = batsmen("Martin Guptill", 3531, 173, 310)

shaheen = bowler("Shaheen Shah", 22, 102)
southee = bowler("Tim Southee", 22, 164)
arshdeep = bowler("Arshdeep", 18, 99)
rabada = bowler("Kagiso Rabada", 27, 71)
malinga = bowler("Lasith Malinga", 21, 107)
hassan = bowler("Hassan Ali", 23, 60)

zampa = bowler("Adam Zampa", 17, 106)
shamsi = bowler("Tabraiz Shamsi", 18, 89)
shadab = bowler("Shadab Khan", 20, 97)
rashid = bowler("Rashid Khan", 19, 130)
adil = bowler("Adil Rashid", 21, 96)
hasaranga = bowler("Hasaranga", 18, 92)

rizwan = keeper("Mohammad Rizwan", 41, 11)
dhoni = keeper("MS Dhoni", 57, 34)
ramdin = keeper("Denesh Ramdin", 43, 20)
dekock = keeper("Q de Kock", 84, 18)
rahim = keeper("Mushfiqur Rahim", 32, 30)

# Player pools
batters =  [babar, rohit, fakhar, virat, warner, abd, guptil, pooran, buttler]
pacers =   [southee, shaheen, arshdeep, rabada, malinga, hassan]
spinners = [zampa, shamsi, shadab, rashid, adil, hasaranga]
keepers =  [rizwan, dhoni, ramdin, dekock, rahim]

random.shuffle(batters)
random.shuffle(pacers)
random.shuffle(spinners)
random.shuffle(keepers)

# Game setup
purse1 = 100
purse2 = 100
squad1 = []
squad2 = []

print("------------------------------------------------------")
print("| Welcome To the Auction OF Global Club Championship |")
print("------------------------------------------------------")
name1 = input(" Enter P1 Team Name :| ")
name2 = input(" Enter P2 Team Name :| ")
print("------------------------------------------------------")
print("| Both Team Purse Is :-  $100 |")

time.sleep(2)

maximum=6
# Auction function
def auction_round(player_list, role_name):
    global purse1, purse2
    print(f"\n-- Round: {role_name} --")
    if not player_list:
        print("No players left in this category.")
        return

    player = player_list.pop(0)
    print(f"Player up for bid: {player}")
    print("-----------------------------------")
    time.sleep(2)
    print     ("| Do You Want To skip This Player ...... |")
    skip=input("| To Skip Press 'S' | else Press any Key To Continus |")
    print("-----------------------------------")
    print()

    if skip == "S" or skip == "s":
        return
    
    try:
        
        bid1 = int(input(f"{name1} Bid: "))
        if bid1 > purse1:
            print("Insufficient funds!")
            bid1 = 0
    except:
        bid1 = 0

    try:
        bid2 = int(input(f"{name2} Bid: "))
    
        if bid2 > purse2:
            print("Insufficient funds!")
            bid2 = 0
    except:
        bid2 = 0
    
    if bid1 == bid2:
        winner = random.choice([1, 2])
        if winner == 1:
     
            if len(squad1) > maximum:
              print(f"{name1} Squad Is Full ...... Limit Is Exceded")
            else:
             squad1.append(player)
             purse1 -= bid1
             print()
             print(f"{player} goes to {name1} (random tiebreak)")
        else:
     
            if len(squad2) > maximum:
              print(f"{name2} Squad Is Full ...... Limit Is Exceded")
            else :
             squad2.append(player)
             purse2 -= bid2
             print()
             print(f"{player} goes to {name2} (random tiebreak)")
    
    elif bid1 > bid2:
        if len(squad1) > maximum:
              print(f"{name1} Squad Is Full ...... Limit Is Exceded")
        else:
          squad1.append(player)
          purse1 -= bid1
          print()
          print(f"{player} goes to {name1}")
    else:
        if len(squad2) > maximum:
            print(f"{name2} Squad Is Full ...... Limit Is Exceded")
        else :
            squad2.append(player)
            purse2 -= bid2
            print()
            print(f"{player} goes to {name2}")
    
    SquadNum1= len(squad1)
    SquadNum2= len(squad2)
    

    print("-----------------------------------------------------")
    print(f"|     {name1} Purse: ${bid1}      |    {name2} Purse:   ${bid2}   | ")
    print("-----------------------------------------------------") 
    print(f"|     {name1} Purse: ${purse1}      |     {name2} Purse: ${purse2}   | ")
    print("-----------------------------------------------------")
    print(f"| Player in {name1} Squad '{SquadNum1}' | Player in {name2} Squad '{SquadNum2}' |") 
    print("-----------------------------------------------------")

# Example: Change the number of rounds here
for _ in range(8):  # 8 batters will be auctioned
    auction_round(batters, "Batsman")

for _ in range(5):  # 5 pacers will be auctioned
    auction_round(pacers, "Pacer")

for _ in range(5):  # 5 spinners will be auctioned
    auction_round(spinners, "Spinner")

for _ in range(4):  # 3 keeper will be auctioned
    auction_round(keepers, "Wicket Keeper")

# Show Squads
print("------------------------------------------------------")
print(f"{name1} SQUAD:", end=" ")
for a in squad1:
    print(a, end=" | ")
print()
print(f"{name2} SQUAD:", end=" ")
for b in squad2:
    print(b, end=" | ")
print("\n------------------------------------------------------")

# Scoring
def calculate_score(squad):
    Batting = Bowling = Keeping = 0
    for p in squad:
        if isinstance(p, batsmen):
            r1 = p.run / 2
            b1 = p.sixes + p.four
            Batting += r1 + b1
        elif isinstance(p, bowler):
            w1 = p.wickets
            if p.average > 22:
                a1 = 100
            elif p.average > 20:
                a1 = 200
            else:
                a1 = 300
            Bowling += w1 + a1
        elif isinstance(p, keeper):
            k1 = p.catches + p.stumping
            Keeping += k1
    return Batting, Bowling, Keeping

# Score Summary
bat1, bowl1, keep1 = calculate_score(squad1)
bat2, bowl2, keep2 = calculate_score(squad2)
total1 = bat1 + bowl1 + keep1
total2 = bat2 + bowl2 + keep2

print(f"\n{name1} => Batting: {bat1:.1f} | Bowling: {bowl1} | Keeping: {keep1} | Total: {total1}")
time.sleep(3)
print(f"{name2}   => Batting: {bat2:.1f} | Bowling: {bowl2} | Keeping: {keep2} | Total: {total2}")
print("--------------------------------------------------------")

winner = ""

# Result
if total1 > total2:
    winner = name2
    print(f"Team One Score {total1}")
    time.sleep(2)
    print(f"Team One Score {total2}")
    print(f"🏆 {winner} Wins the Match!")

elif total2 > total1:
    winner = name2
    print(f"Team One Score {total1}")
    time.sleep(2)
    print(f"Team One Score {total2}")
    print(f"🏆 {winner} Wins the Match!")

else:
    print(f"Team One Score {total1}")
    time.sleep(2)
    print(f"Team One Score {total2}")
    print("Match Tied!")

Played_time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

Result_2P_auction = "C:\\Users\\mansoor\\Desktop\\Result OF Programs\\2P Auction Result"

with open(Result_2P_auction, "a")as file:
    file.write(f"\n--{name1} Total : {total1} ")
    file.write(f"\n--{name2} Total : {total2} ")
    file.write("\n----------------------------------------")
    file.write(f"\n--{winner} Is the Winner ")
    file.write(f"\n--This Match Is being played at {Played_time}")
    file.write("\n")