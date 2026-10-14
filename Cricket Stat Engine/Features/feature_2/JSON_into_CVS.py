import json, os,csv

directory = r"Portfolio\Cricket Stat Engine\JSon Raw Data"
player_stat = {}
country_files = {
    "Pakistan"      : r"Portfolio\Cricket Stat Engine\Processed Stat\Player Stats\Country Vise\PAK.csv",
    "India"         : r"Portfolio\Cricket Stat Engine\Processed Stat\Player Stats\Country Vise\IND.csv",
    "England"       : r"Portfolio\Cricket Stat Engine\Processed Stat\Player Stats\Country Vise\ENG.csv",
    "Australia"     : r"Portfolio\Cricket Stat Engine\Processed Stat\Player Stats\Country Vise\AUS.csv",
    "South Africa"  : r"Portfolio\Cricket Stat Engine\Processed Stat\Player Stats\Country Vise\SA.csv",
    "New Zealand"   : r"Portfolio\Cricket Stat Engine\Processed Stat\Player Stats\Country Vise\NZ.csv",
    "Sri Lanka"     : r"Portfolio\Cricket Stat Engine\Processed Stat\Player Stats\Country Vise\SRI.csv",
    "Bangladesh"    : r"Portfolio\Cricket Stat Engine\Processed Stat\Player Stats\Country Vise\BAN.csv"
}
# -----------------| HELPERS |-----------------

def update_batting(player, runs, balls):
    if player in player_stat:
        player_stat[player]["runs"] += runs
        player_stat[player]["balls"] += balls

def update_bowling(player, runs_conceded, balls_bowled, wickets):
    if player in player_stat:
        player_stat[player]["runs_conceded"] += runs_conceded
        player_stat[player]["balls_bowled"] += balls_bowled
        player_stat[player]["wickets"] += wickets

def update_out(player):
    if player in player_stat:
        player_stat[player]["outs"] += 1

# -----------------| MAIN PROCESS |-----------------
def ProcessData(data):
    players = data["info"]["players"]
    motm    = data["info"].get("player_of_match" , [])
    match_runs = {}

    # ---------- INIT + MATCH COUNT ----------
    for team, squad in players.items():
        for player_name in squad:

            if player_name not in player_stat:
                player_stat[player_name] = {
                    "nation": team,
                    "matches": 0,
                    "MOTM":0,
                    
                    # batting
                    "runs": 0,
                    "balls": 0,
                    "outs": 0,
                    "highest_score": 0,
                    "strike_rate": 0,
                    "100s":0,
                    "50s":0,

                    # bowling
                    "wickets": 0,
                    "runs_conceded": 0,
                    "balls_bowled": 0,
                    "best_bowling": (0, 0)
                }

            # ✔ match count (correct place)
            player_stat[player_name]["matches"] += 1

    # ---------- PROCESS INNINGS ----------
    innings = data["innings"]

    for inning in innings:
        overs = inning["overs"]

        for over in overs:
            for delivery in over["deliveries"]:

                batter = delivery.get("batter")
                bowler = delivery.get("bowler")

                runs = delivery["runs"]["batter"]
                total_runs = delivery["runs"]["total"]

                # BATSMAN
                update_batting(batter, runs, 1)

                if batter not in match_runs:
                    match_runs[batter] = 0

                match_runs[batter] += runs

                # BOWLER
                update_bowling(bowler, total_runs, 1, 0)

                # WICKET
                if "wickets" in delivery:
                    for w in delivery["wickets"]:
                        out_player = w.get("player_out")
                        update_out(out_player)
                        update_bowling(bowler, 0, 0, 1)

    # ---------- POST MATCH CALCULATIONS ----------

    for player, stat in player_stat.items():
    # strike rate
        if stat["balls"] > 0:
            stat["strike_rate"] = round((stat["runs"] / stat["balls"]) * 100, 2)
        else:
            stat["strike_rate"] = 0
    
    # economy 
        if stat["balls_bowled"] > 0:
            stat["economy"] = round(stat["runs_conceded"] / (stat["balls_bowled"] / 6) , 2)
        else:
            stat["economy"] = 0

    # Batting Average 
        if stat["outs"] > 0:
            stat["bat_avg"] = round(stat["runs"] / stat["outs"] , 2)
        else :
            stat["bat_avg"] = stat["runs"]    
    #Bowler Average
        # If a player has no wickets, store runs_conceded as a placeholder
        # to avoid division-by-zero in later rating calculations.

        if stat["wickets"] > 0:
            stat["ball_avg"] = round(stat["runs_conceded"] / stat["wickets"] , 2)
        else :
            stat["ball_avg"] =  float("inf")

    # Man of the Match
    for player in motm:
        if player in player_stat:
            player_stat[player]["MOTM"] += 1

    # highest score (match-based)
    for player, runs in match_runs.items():
        if runs >= 100 :
            player_stat[player]["100s"] += 1

        elif runs >= 50 :
            player_stat[player]["50s"] += 1    
        
        if runs > player_stat[player]["highest_score"]:
            player_stat[player]["highest_score"] = runs

def RatingCalculate():  
        for player, stat in player_stat.items():
 
            runs         = int(stat["runs"])
            wickets      = int(stat["wickets"])
            matches      = int(stat["matches"])
            balls_bowled = int(stat["balls_bowled"]) 
            balls_faced  = int(stat["balls"])
            out          = int(stat["outs"])
            motm         = int(stat["MOTM"])
            
            if matches < 20:  
                Bowling_BPM = balls_bowled/matches # Balls Bowled Per Match
                Batting_BPM = balls_faced/matches  # Balls Batted Per Match
                
                if Bowling_BPM >= 12 and Batting_BPM >= 15:
                    role = "All-rounder"
                elif Bowling_BPM >= 12:
                    role = "Bowler"
                else:
                    role = "Batter"
            # For Experinced (Old)
            else:
                if wickets >= 25 and runs >= 400:
                    role = "All-rounder"
                elif wickets >= 35:
                    role = "Bowler"
                else:
                    role = "Batter"
            SR_Multiply = stat["strike_rate"] /45
            bat_rating  = round((runs / 2 +            
                                   stat["bat_avg"] * 25 +
                                   stat["100s"] *50 +        
                                   stat["50s"]  *30 +                    
                                   stat["strike_rate"] * SR_Multiply) - matches * 2 , 2)  
            
            bowl_rating  = round((wickets * 30  -     
                                  ((stat["economy"] * 4 ) + (stat["ball_avg"] * 3 ) ) ) - matches * 2 , 2)
            
            if motm > 1:
               MOTM_rating = round(stat["MOTM"] * 20 , 2)
            else :
                MOTM_rating = 10
            
            AR_rating    = round( bat_rating + bowl_rating + MOTM_rating , 2)

            if role == "Batter":
                stat["rating"] = round(bat_rating , 2)
                stat["role"]   = role
                
            elif role == "Bowler":
                stat["rating"] = round(bowl_rating, 2)
                stat["role"]   = role
            
            elif role == "All-rounder":   
                stat["role"]   = role
                stat["rating"] = round(AR_rating / 1.3, 2)

# -----------------| LOADING FILES |-----------------

def Loading():
    for filename in os.listdir(directory):
            with open(f"{directory}/{filename}", "r") as f:
                data = json.load(f)
                ProcessData(data)

# ----------------| CSV FILES CONVERSION |-------------------

def CreateHeaders():

    for filename in country_files.values():

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow([
                "Player",
                "Role",
                "Matches",
                "MOTM",
                "Runs",
                "Balls",
                "Outs",
                "Batting Avg",
                "100s",
                "50s",
                "Highest Score",
                "Strike Rate",
                "Wickets",
                "Economy",
                "Bowling Avg",
                "Runs Conceded",
                "Balls Bowled",
                "Rating"           
            ])

def SaveToCSV(nations):
    for player, stat in player_stat.items():

        filename = nations.get(stat["nation"])

        if filename is None:
            continue

        with open(filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow([
                player,
                stat["role"],
                stat["matches"],
                stat["MOTM"],
                stat["runs"],
                stat["balls"],
                stat["outs"],
                stat["bat_avg"],
                stat["100s"],
                stat["50s"],
                stat["highest_score"],
                stat["strike_rate"],
                stat["wickets"],
                stat["economy"],
                stat["ball_avg"],
                stat["runs_conceded"],
                stat["balls_bowled"],
                stat["rating"]
            ])

# -----------------| OUTPUT |-----------------

CreateHeaders()
Loading()
RatingCalculate()
SaveToCSV(country_files)