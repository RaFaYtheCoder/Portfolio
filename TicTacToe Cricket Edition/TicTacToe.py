from functools import partial 
from tkinter import  *
import random

player_turn     = 1      # start with Player 1
turn            = "X"    # Player 1 starts with X
turn_label      = None   # will store Trun Display Label
guess_display   = None   # WIll Store Guess Display label
comp_guess=""
# Records for the game
scorer=   {"Australia":["warner","maxwell","finch"],
           "South\nAfrica":["kock","miller","reeza"],
           "England":["buttler","morgan","hales"],
           "India":["rohit","virat","surya"],
           "Pakistan":["babar","rizwan","hafeez"]}

wc_scorer={"Australia":["warner","watson","maxwell"],
           "South\nAfrica":["abd","kock","duminy"],
           "England":["buttler","kevin","hales"],
           "India":["virat","rohit","yuvraj"],
           "Pakistan":["kamran","afridi","malik"]}

wc_bowler={"Australia":["starc","zampa","watson"],
           "South\nAfrica":["nortje","morkel","steyn"],
           "England":["broad","adil","jardan"],
           "India":["ashwin","jadeja","harbhajan"],
           "Pakistan":["afridi","ajmal","gul"]}

bowler=   {"Australia":["zampa","josh","cummins"],
           "South\nAfrica":["shamsi","rabada","nortje"],
           "England":["broad","adil","jordan"],
           "India":["arshdeep","bhuvi","hardik"],
           "Pakistan":["shadab","shaheen","rauf"]}

centuries={"Australia":["ponting","waugh","finch"],
           "South\nAfrica":["amla","abd","faf"],
           "England":["jonny","roy","root"],
           "India":["rohit","virat","sachin"],
           "Pakistan":["yousaf","babar","anwer"]}

# Combine all records in list
all_records = [scorer, centuries, bowler, wc_scorer, wc_bowler]
records_labels = ["Top3 Scorer\nIn T20i", "Top3 in\nCenturies ODi", "Top3 Bowlers\nin T20i", 
                  "Top3 Scorers\nIn T20 WC", "Top3 Bowlers\nIn T20 WC"]

#Teams For the Grid Question
teams = ["Australia", "South\nAfrica", "England", "India", "Pakistan"]

# GUI Setup
button_entries = {}
buttons = {}
index_record = []
index_teams = []

window1 = Tk()
window1.title("Cricket Guess Grid")

# Shuffle and select 3 records and teams
record_indices = random.sample(range(5), 3)
team_indices = random.sample(range(5), 3)

selected_records = [records_labels[i] for i in record_indices]
selected_teams = [teams[i] for i in team_indices]

# Debug print to see shuffled order
print("Selected Records:", selected_records)
print("Selected Teams:", selected_teams)

# Entry popup window
def guessing(r, c):
    global ans,turn_label
    
    window2 = Toplevel()
    window2.geometry("400x135")
    Label(window2, text=f"Enter Player for Button {r},{c}:", font=("ariel", 15)).grid(column=0, row=0)
    ans = Entry(window2, width=25, font=("ariel", 25))
    ans.grid(column=0, row=1)
    Button(window2, text=" Enter ", font=("ariel", 15),
           command=lambda: main(r, c),
           relief=GROOVE, bd=10, padx=10, pady=8).grid(column=0, row=2)
    turn_label = Label(window1, text=f"Player 1 Turn ( O )", font=("ariel", 20), 
                                 relief=RAISED, bd=10,padx=8,pady=4)
    turn_label.grid(row=4, column=0, columnspan=2)

# Logic when entry is submitted
turn = "O" 
def main(r, c):
    global turn_label, player_turn, turn, guess_display,comp_guess

    if guess_display:
        guess_display.destroy()
    
    guess = ans.get().lower()
    print(f"Button {r},{c} Entry: {guess}")

    button_entries[(r, c)] = guess

    record_index = record_indices[r]
    team_index = team_indices[c]

    print()
    print(f"Record at row {r}: {records_labels[record_index]} (Index: {record_index})")
    print(f"Team at column {c}: {teams[team_index]} (Index: {team_index})")
    print()

    record_dict = all_records[record_index]
    team_name = teams[team_index]
    players = record_dict[team_name]

    print(f"Players to match: {players}")
    
    if guess in players:       
        random.shuffle(players)
        comp_guess = players[1]    
        if turn == "O":
            if guess == comp_guess:
                buttons[(r, c)].config(text="❌", state=DISABLED)
            elif guess  !=  comp_guess:
                buttons[(r, c)].config(text="⭕", state=DISABLED)    
            else:
                buttons[(r, c)].config(text="", state=DISABLED)    
            turn_label.config(text="Player 2 Turn ( X )")
            turn ="X"
        
        elif turn == "X":    
            if guess == comp_guess:
                buttons[(r, c)].config(text="⭕", state=DISABLED)
            elif guess  !=  comp_guess:
                buttons[(r, c)].config(text="❌", state=DISABLED)    
            else:
                buttons[(r, c)].config(text="", state=DISABLED)
            turn_label.config(text="Player 1 Turn ( O )")
            player_turn = 1
            turn ="O"
    else:        
            if turn == "O":
                buttons[(r, c)].config(text="")
                turn_label.config(text="Player 2 Turn ( X )")
                turn = "X"
            
            elif turn == "X":
                buttons[(r, c)].config(text="")
                turn_label.config(text="Player 1 Turn ( O )")
                turn = "O"
    guess_display= Label(window1, text=f" Guess Was : {comp_guess}", font=("ariel", 20), 
                                 relief=RAISED, bd=10,padx=8,pady=4)
    guess_display.grid(row=4, column=2, columnspan=2)

# GUI layout
row_labels = [''] + selected_records
col_labels = [''] + selected_teams

# Row labels Question
for r in range(4):
    Label(window1, text=row_labels[r], font=("ariel", 15), relief=RIDGE, bd=10, width=16, height=3)\
        .grid(row=r, column=0)

# Column labels Question
for c in range(4):
    Label(window1, text=col_labels[c], font=("ariel", 15), relief=RIDGE, bd=10, width=12, height=3)\
        .grid(row=0, column=c)

# 3x3 Grid Buttons
for r in range(1, 4):
    for c in range(1, 4):
        btn = Button(window1, text="", font=("ariel", 15), relief=RAISED, bd=10,
                     width=12, height=3, command=partial(guessing, r - 1, c - 1))
        btn.grid(row=r, column=c)
        buttons[(r - 1, c - 1)] = btn

# Top-left white cell
Label(window1, bg="white", width=28, height=6).grid(row=0, column=0)


window1.mainloop()

# git add "TicTacToe Cricket Edition"
# fit comment -m "New Project"
