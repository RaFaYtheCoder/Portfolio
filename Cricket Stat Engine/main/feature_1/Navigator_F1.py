import json,os
directory = r"Portfolio\Cricket Stat Engine\JSon Raw Data" 
teams     = ["Bangladesh","New Zealand","India","England","Australia"
            ,"Pakistan","Sri Lanka","West Indies","South Africa"]

def TeamNames():
    print("="*40)
    for index,value in enumerate(teams):
        index = int(index)
        print(f"{index+1}. {value}")

    print()
    print("-"*40)
    user_i = int(input(" Your selection :"))

    sel_team = teams[user_i-1]
    print(f"You have selected {sel_team}")
    return sel_team

def TeamData(NationName):
    team_data = []
    for filename in os.listdir(directory):
        with open(f"{directory}/{filename}","r") as f:
            data = json.load(f)
    
        teams = data["info"]["teams"]
        if NationName in teams:
            Venue = data["info"]["venue"]
            City = data["info"].get("city", "Unknown")
            team_data.append({  "date"      : data["info"]["dates"],
                                "teams"     : data["info"]["teams"],
                                "venue"     : f"{Venue} , {City}", 
                                "filename"  : filename })
    return team_data        

def TeamYear():
    while True:    
        print("="*56)
        sel_year = int(input("Selecton Year (2007 - 2025) : "))    
        print()
        if sel_year >= 2007 and sel_year < 2026: 
            return sel_year
        else :
            print(" Please Select From Year 2007 TO 2025 !!!")

def TeamFixture(matches,year):
    filtered_matches = []
    for match in matches:
        if str(year) in match["date"][0]:
            filtered_matches.append(match)
    return filtered_matches

def TeamMatch(Filter_list):
    for i, match in enumerate(Filter_list):

        team1    = match["teams"][0]
        team2    = match["teams"][1]
        date     = match["date" ][0]
        venue    = match["venue"]
        FileName = match["filename"]
        print("-"*57)
        print(f"({FileName}| {i+1}). {team1} vs {team2} ({date}) | venue :{venue}")

    print()
    print("="*40)
    match_index = int(input("Input the Index : "))
    
    return Filter_list[match_index-1]

def FinalCall(num):
    Team      = TeamNames()
    Fixture   = TeamData(Team)

    if num == 1:
        return Fixture    
    
    Time      = TeamYear() 
    Filter    = TeamFixture(Fixture,Time)
    
    if num == 2:
        return Filter
    
    sel_match = TeamMatch(Filter)
    
    if num == 3:        
        return sel_match

