# 🏏 Cricket Auction & Match Simulator

## 📜 License
This project is open-source. You are free to use, modify, and share it.  

---

## 🏆 Author
Developed by **Rafay** as part of Python practice projects.  

## 🔥 About the Project

This is a **2-player Python console game** where users participate in an auction to buy cricketers using a limited budget. The players are divided into categories like **batsmen, pacers, spinners, and wicket keepers**. After all rounds, a **scoring system** evaluates each squad and declares a winner.

---

## 🙌 Author
**Built by Rafay** 

– learning Python since July 2025. Keep building!



## 🎮 Features

- 🧠 **Auction-Based Selection** system
- 💰 **Budget Control** for both players ($100 each)
- ⚡ **Squad Limit** to prevent overspending
- ⏭️ **Skip Player Option** during auction
- 🧮 **Custom Scoring Logic** for batsmen, bowlers, and keepers
- ⌛ **Real-time Delay & Input Prompts** for better interaction
- 🧑‍🤝‍🧑 **2-Player Mode** in the terminal


## 🧠 Game Flow

### Enter Team Names.

- 4 rounds:

1. Batsmen

2. Pacers

3. Spinners

4. Keepers

- Each round shows a random player.

- Players can bid or skip.

- If both bids match, random tiebreaker decides.

- Score is calculated based on players’ stats.

- The higher scoring team wins!

## 🧮 Scoring System
- Batting:

1. Runs: runs / 2

2. Sixes: +1 each

3. Fours: +1 each

- Bowling:

1. Wickets: +1 each

- Average:

1. 22 ➝ +100

2. 20 ➝ +200

3. ≤20 ➝ +300

- Keeping:

1. Catches + Stumpings = Score

# 📋 Example Output

                         -- Round: Batsman --

Player up for bid: Virat Kohli

Team1 Bid: 30

Team2 Bid: 25

Virat Kohli goes to Team1!

...

Team1 => Batting: 4267.0 | Bowling: 390 | Keeping: 50 | Total: 4707.0
Team2 => Batting: 3920.0 | Bowling: 450 | Keeping: 55 | Total: 4425.0

🏆 Team1 Wins the Match!
