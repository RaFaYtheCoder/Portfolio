import csv 
 
def DictToCSV(data): 
 
    with open(r"Data\CSV Files\Staduim Stats\stadium_stats.csv", "w", newline="", encoding="utf-8") as f: 
 
        writer = csv.writer(f) 
 
        # --------- Header ---------------- 
        writer.writerow([ 
            "Venue", 
            "City",
            "Country",
            "Matches", 
            "Innings 1 Runs", 
            "Innings 2 Runs", 
            "Innings 1 Wickets", 
            "Innings 2 Wickets", 
            "Highest Total", 
            "Lowest Total", 
            "Bat First Wins", 
            "Chase Wins" 
        ]) 
 
        # --------- Data ------------------ 
        for venue, stats in data.items(): 
 
            writer.writerow([ 
                venue, 
                stats["city"],
                stats["country"],
                stats["matches"], 
                stats["innings_1_runs"], 
                stats["innings_2_runs"], 
                stats["innings_1_wickets"], 
                stats["innings_2_wickets"], 
                stats["highest_total"], 
                stats["lowest_total"], 
                stats["bat_first_wins"], 
                stats["chase_wins"] 
            ])