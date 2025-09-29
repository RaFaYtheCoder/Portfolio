# 🏏 Two-Player Cricket Squad Selection Game (Python Console)

## 📜 License
This project is open-source. You are free to use, modify, and share it.  

---

## 🏆 Author
Developed by **Rafay** as part of Python practice projects.  


## 📋 Overview
This is a two-player Python console game where each player selects their dream cricket squad consisting of **batsmen**, **bowlers**, and **wicketkeepers**. After selecting players, both players choose specific stats from their players to form a cumulative score. The player with the higher score **wins**.

---

## 🎮 How to Play
1. **Player 1** and **Player 2** take turns.
2. Each player builds a 5-player squad by selecting:
   - 2 Batsmen
   - 1 Wicketkeeper
   - 1 Spinner
   - 1 Pacer
3. Each player is shown their squad's stats for 5 seconds.
4. After both players select, they choose **one stat per player** to compete.
5. Scores are calculated based on chosen stats.
6. The player with the higher score **wins**.

---

## ⚙️ How to Run
Ensure you have Python installed (3.6+ recommended).


## 👤 Player Types
 - Batsmen: Evaluated by Runs, Strike Rate (SR),    Sixes, Fours

 - Bowlers: Evaluated by Wickets, Average, Economy, Hauls
 
 - Wicketkeepers: Evaluated by Catches, Stumpings

## 💡 Features
Uses random.shuffle() to ensure varied player options each round.

Clears screen after selections to avoid peeking.

Summarizes and compares both players' scores.

Cleanly structured using OOP principles: batsmen, bowler, keeper classes

## 📌 Dependencies
time (built-in)

os (built-in)

random (built-in)

