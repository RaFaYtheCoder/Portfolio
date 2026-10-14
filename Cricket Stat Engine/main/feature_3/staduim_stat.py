import time,os,json
from csv_converter import DictToCSV

directory       = r"Portfolio\Cricket Stat Engine\JSon Raw Dat" 
Stadium_Stat    =  {}

venue_alias = {
    "R Premadasa Stadium"       : ["R Premadasa Stadium", "R.Premadasa Stadium"],
    "M Chinnaswamy Stadium"     : ["M Chinnaswamy Stadium", "M.Chinnaswamy Stadium"],
    "The Wanderers Stadium"     : ["The Wanderers Stadium", "New Wanderers Stadium"],
    "National Cricket Stadium"  : ["National Cricket Stadium", "National Stadium"],
    "Bready Cricket Club"       : ["Bready Cricket Club", "Bready"],
    "Darren Sammy National Cricket Stadium" : ["Darren Sammy National Cricket Stadium", "Daren Sammy National Cricket Stadium"],
    "Sylhet International Cricket Stadium"  : ["Sylhet Stadium", "Sylhet International Cricket Stadium"],
    "Sheikh Zayed Stadium"  : ["Sheikh Zayed Stadium", "Zayed Cricket Stadium"],
    "Narendra Modi Stadium" : ["Narendra Modi Stadium", "Sardar Patel Stadium"],
    "The Village"           : ["The Village", "Malahide"]}

def OverallStat( venue , runs , wicket , inning_status ):

    if    inning_status == 1:
        Stadium_Stat[venue]["innings_1_runs"] += runs
        Stadium_Stat[venue]["innings_1_wickets"] += wicket
        
    elif  inning_status == 2:
        Stadium_Stat[venue]["innings_2_runs"] += runs
        Stadium_Stat[venue]["innings_2_wickets"] += wicket

def HighestLowest(venue , score):

    if Stadium_Stat[venue]["lowest_total"] == 0 and Stadium_Stat[venue]["highest_total"] == 0:
        Stadium_Stat[venue]["lowest_total"]  = score  
        Stadium_Stat[venue]["highest_total"] = score

    else :
        if  score > Stadium_Stat[venue]["highest_total"] :
              Stadium_Stat[venue]["highest_total"] = score

        if score < Stadium_Stat[venue]["lowest_total"]:
            Stadium_Stat[venue]["lowest_total"] = score

def Winning(venue , winning_inning):
    if winning_inning == 1:
        Stadium_Stat[venue]["bat_first_wins"] += 1

    elif winning_inning == 2:
        Stadium_Stat[venue]["chase_wins"] += 1        
    
def LoadingData(dir):
    for index, filename in enumerate(os.listdir(dir)[::-1]):
        with open(f"{dir}/{filename}","r") as f:
            data    = json.load(f)
            outcome = data["info"].get("outcome")
        if outcome and outcome.get("result") not in ["no result", "tie"]:
            StatComputation(data)

def CityGetter(venue,city):
    Stadium_Stat[venue]["city"] = city


def StatComputation(Data):
    venue = Data["info"]["venue"]

# --------- Name Addition ----------------
    if "," in venue :  comma_index =  venue.find(",")
    else            :  comma_index =  len(venue)
    venue = venue[:comma_index]
    
    for index,value in venue_alias.items():
        for names in value:
            if venue == names:
                venue = index
                break


# --------- Initilization -----------
    if not venue in Stadium_Stat:
        Stadium_Stat[venue] = { # Variabale of the stats
        "matches": 0,
        "city"  :0,
        "country":0,

        "innings_1_runs"    : 0,
        "innings_2_runs"    : 0,
        "innings_1_wickets" : 0,
        "innings_2_wickets" : 0,
        "highest_total" : 0,
        "lowest_total"  : 0,    
        
        "bat_first_wins": 0,
        "chase_wins": 0}
    
   
    Stadium_Stat[venue]["matches"] += 1

    innings      =  Data["innings"]
    outcome      =  Data["info"].get("outcome")
    city         =  Data["info"].get("city" , "Unknown")

    if outcome:
        outcome = outcome["by"]

        if outcome.get("runs"):
            winning_inning = 1  

        elif outcome.get("wickets"):
            winning_inning = 2


    for index,inning in enumerate( innings, start= 1):
        if   index == 1 :   inning_status = 1
        elif index == 2 :   inning_status = 2    

        inning_score = 0 
        overs = inning["overs"]

        for over in overs:
            for delivery in over["deliveries"]:

                runs = delivery["runs"]["total"]
                if delivery.get("wickets") :   wicket = 1
                else                       :   wicket = 0    

                inning_score += runs

                OverallStat(venue , runs ,  wicket , inning_status)

        HighestLowest( venue , inning_score)        

    if Stadium_Stat[venue]["city"] == 0 or Stadium_Stat[venue]["city"] == "Unknown":
        CityGetter(venue,city)

    if outcome:
        Winning(venue , winning_inning )


def F3_Calling():
    LoadingData(directory)
    DictToCSV(Stadium_Stat)
    print("Done")

F3_Calling()