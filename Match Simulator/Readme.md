# 🏏 Cricket Match Simulator (Python)

## 📜 License
This project is open-source. You are free to use, modify, and share it.  

---

## 🏆 Author
Developed by **Rafay** as part of Python practice projects.  


A **text-based 2-player cricket match simulator** built in Python.  
Players select their teams, toss the coin, and play through randomized ball-by-ball commentary with results at the end.  

---

## 🎮 Features
- **Team Selection**  
  - Each player selects batters, pacers, spinners, and a wicketkeeper from a random pool.  

- **Toss Simulation**  
  - Random toss with a choice to **bat** or **bowl** first.  

- **Ball-by-Ball Commentary**  
  - Random outcomes like:
    - Dot ball  
    - Single, Double, Triple  
    - Four, Six  
    - Wicket  
    - Overthrows (5 runs)  

- **Two Innings**  
  - Both teams play one innings each.  
  - Winner decided by runs or wickets margin.  

- **Dynamic Commentary**  
  - Player names included in every ball description.  

---

## ⚡ How It Works
1. Run the Python file.  
2. Both players enter their **team names**.  
3. Each player selects their **squad** from shuffled lists of players.  
4. A toss decides who bats/bowls first.  
5. The match begins with **12 balls per innings** (you can extend overs easily).  
6. Randomized outcomes simulate the match ball by ball.  
7. At the end, the program announces the **winner**.  

---

## 🖥️ Example Gameplay

Enter Player 1 Team Name |: Thunder Kings
Enter Player 2 Team Name |: Fire Warriors

Team 1 Selection
| Babar Azam | Rohit Sharma |
Enter Your Selection :| Babar Azam
Fakhar Zaman | Virat Kholi |
Enter Your Selection :| Virat Kholi
******* Toss Time ********

Head Is the call !!!!!!
and Head it is
Thunder Kings Won The Toss And Elected To batting
Thunder Kings Decided To Bat First

Ball 1
Babar Azam Plays A Beautiful Shot straight Down the Ground For Four Runs

Thunder Kings | 4/0 in 1 Balls


---

## 🚀 Future Improvements
- Add support for **multiple overs** instead of fixed 12 balls.  
- Save **match results to a text/CSV file** for history.  
- Add **scoreboard display** after each over.  
- Create a **GUI version** using Tkinter or PyQt.  

---


