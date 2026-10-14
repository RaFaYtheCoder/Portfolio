from Navigator_F1 import FinalCall
import json,os,time

directory = r"Portfolio\Cricket Stat Engine\JSon Raw Data" 

def LoadingData(FileName):    
    with open(f"{directory}/{FileName}","r") as f:
                data = json.load(f)

    return data

def MatchInfo(num,winner,result,toss,toss_sel,man_of_match,series,match_num):
    if  "runs"   in result:
        result_way = "RUNS"
        margin     = result["runs"]

    elif "wickets" in result:
        result_way = "WICKETS"     
        margin     = result["wickets"]
    
    if num == 1:
        print("-"*60)
        print(f"{series} --- Match NO.{match_num}")
        time.sleep(2)
        print(f"Toss won by {toss} and elected to {toss_sel.upper()}")
    elif num == 2:
        print("-"*60)
        print(f"{winner} Won the match by {margin} {result_way} ")
        time.sleep(2)
        print(f"Player of the Match is : {man_of_match} ")

def MatchExtras(batting_scoreboard,bowling_scoreboard,batter,bowler,balls,num):
 
    if num == 1: # legal Bowl
        batting_scoreboard[batter]["runs"]    +=   balls["runs"]["batter"] 
        bowling_scoreboard[bowler]["runs"]    +=   balls["runs"]["batter"]  
        batting_scoreboard[batter]["balls"]   +=   1     
        bowling_scoreboard[bowler]["balls"]   +=   1    

    elif num == 2: # Wide
        bowling_scoreboard[bowler]["runs"]   +=   balls["runs"]["total"]                        

    elif num == 3: # No Ball
        batting_scoreboard[batter]["runs"]  +=   balls["runs"]["batter"] 
        bowling_scoreboard[bowler]["runs"]  +=   balls["runs"]["total"]         
         
    elif num == 4: # Byes
        batting_scoreboard[batter]["balls"]   +=   1     
        bowling_scoreboard[bowler]["balls"]   +=   1    

    elif num == 5: # LegByes
        batting_scoreboard[batter]["balls"]   +=   1     
        bowling_scoreboard[bowler]["balls"]   +=   1     

def MatchToss(toss,toss_sel,teams):
    for team in teams:
        if team == toss and toss_sel == "bat":
            BatFirst = team

        elif team != toss and toss_sel == "field":
            BatFirst = team
    
    return BatFirst

def MatchInning(innings):
    
    batting_scoreboard = {}
    bowling_scoreboard = {}
    inning_stat        = []

    for inning in innings:
        inning_total = { 
            "total"   : 0 ,
            "wickets" : 0  }
        
        overs = inning["overs"]
        for over in overs:
            for balls in over["deliveries"]:
#Player-Storage 
                batter = balls["batter"]
                bowler = balls["bowler"]

                if not batter in batting_scoreboard:
                     batting_scoreboard[batter] ={
                       "runs"  :  0,
                       "balls" :  0,
                       "SR"    :  0,
                       "out"   :  0 
                     }
                
                if not bowler in bowling_scoreboard:
                     bowling_scoreboard[bowler] ={
                       "balls"    :  0,
                       "runs"     :  0,
                       "economy"  :  0,
                       "wicket"   :  [] 
                     }

#Stats-Storage  
                                    
                if "extras" not in  balls :
                 MatchExtras(batting_scoreboard,bowling_scoreboard,batter,bowler,balls,1)

                elif balls["extras"].get("wides"):
                 MatchExtras(batting_scoreboard,bowling_scoreboard,batter,bowler,balls,2)
                    
                elif balls["extras"].get("noballs"):
                 MatchExtras(batting_scoreboard,bowling_scoreboard,batter,bowler,balls,3)
                    
                elif balls["extras"].get("byes"):
                 MatchExtras(batting_scoreboard,bowling_scoreboard,batter,bowler,balls,4)
                    
                elif balls["extras"].get("legbyes"):
                 MatchExtras(batting_scoreboard,bowling_scoreboard,batter,bowler,balls,5)
                
                if balls.get("wickets"):
                    inning_total["wickets"] += 1
                    wicket     = balls["wickets"][0]
                    wktKind    = wicket["kind"]
                    player_out = wicket["player_out"]

                    batting_scoreboard[player_out]["out"]  = {  
                        "wktKind" : wktKind,
                        "player"  : player_out, 
                        "bowler"  : bowler}
                    
                    bowling_scoreboard[bowler]["wicket"].append({  
                        "wktKind" : wktKind,
                        "player"  : player_out })


                    if wicket.get("fielders"):
                        fielder      = wicket["fielders"][0]
                        fielder_name = fielder["name"]
                        
                        batting_scoreboard[player_out]["out"]["fielder"] = fielder_name                     


                inning_total["total"]   += balls["runs"]["total"]

        inning_stat.append(inning_total)


    scoreboard = [batting_scoreboard,bowling_scoreboard,inning_stat]
    return scoreboard

    pass

def EconomySrCalculate(Scoreboards):
    batting_scorecard  =  Scoreboards[0]
    bowling_scorecard  =  Scoreboards[1]

    for batter,stat in batting_scorecard.items():
        if stat["balls"] > 0:
            stat["SR"] = round((stat["runs"] / stat["balls"])*100, 2)

    for bowler,stat in bowling_scorecard.items():
        if stat["balls"] > 0:
            stat["economy"] = round(stat["runs"] / (stat["balls"] / 6), 2)
    return Scoreboards

def ScoreCardSepration(Scorecards,info,teams):

    squads = info["players"]

    Batting_Card = Scorecards[0]
    Bowling_Card = Scorecards[1]
          
    TeamBat_1    = {}
    TeamBat_2    = {}
    TeamBowl_1   = {}
    TeamBowl_2   = {}

    for name,stat in Batting_Card.items():
        
        if name in squads[teams[0]]:
            TeamBat_1[name] = stat
        
        elif name in squads[teams[1]]:
            TeamBat_2[name] = stat   
                
    for name,stat in Bowling_Card.items():
        
        if name in squads[teams[0]]:
            TeamBowl_1[name] = stat
        
        elif name in squads[teams[1]]:
            TeamBowl_2[name] = stat   
                
    return [TeamBat_1,TeamBat_2,TeamBowl_1,TeamBowl_2]      

def ScorecardDisplay(ScoreCard, num):
    for count, card in enumerate(ScoreCard, start=1):

        if count == num:

            # BATTING CARD
            if count < 3:

                print("|" + "="*105 + "|")
                print(
                    f"| {'Player':<20} | {'Runs':<6} | {'Balls':<7} | "
                    f"{'SR':<7} | {'Dismissal':<45} |"
                )
                print("|" + "="*105 + "|")

                for player, stat in card.items():

                    if stat["out"] == 0:
                        dismissal = "Not Out"
                        player_name = f"{player}*"

                    else:
                        dismissal = stat["out"]["wktKind"]

                        if stat["out"].get("fielder"):
                            dismissal += (
                                f" by {stat['out']['fielder']} "
                                f"b {stat['out']['bowler']}"
                            )
                        else:
                            dismissal += f" b {stat['out']['bowler']}"

                        player_name = player

                    print(
                        f"| {player_name:<20} | "
                        f"{stat['runs']:<6} | "
                        f"{stat['balls']:<7} | "
                        f"{stat['SR']:<7} | "
                        f"{dismissal:<45} |"
                    )

            # BOWLING CARD
            elif count < 5:

                print("|" + "="*80 + "|")
                print(
                    f"| {'Player':<20} | {'Runs':<6} | "
                    f"{'Balls':<7} | {'Wkts':<5} | {'Economy':<7} |"
                )
                print("|" + "="*80 + "|")

                for player, stat in card.items():

                    wickets = len(stat["wicket"])

                    print(
                        f"| {player:<20} | "
                        f"{stat['runs']:<6} | "
                        f"{stat['balls']:<7} | "
                        f"{wickets:<5} | "
                        f"{stat['economy']:<7} |"
                    )
              
def InningDislpay(Summary,inning_total,Batfirst,winner,result,toss,toss_sel,man_of_match,teams,series,match_num):
 if Batfirst == teams[0]:
    Inning1 = teams[0]
    Inning2 = teams[1]

    BatCard1  = 1
    BowlCard1 = 4

    BatCard2  = 2
    BowlCard2 = 3

 else:
    Inning1 = teams[1]
    Inning2 = teams[0]

    BatCard1  = 2
    BowlCard1 = 3

    BatCard2  = 1
    BowlCard2 = 4

  
 MatchInfo(1,winner,result,toss,toss_sel,man_of_match,series,match_num)
 input()
 print(f"|             Inning 1 -- {Inning1}                 ")
 input()
 ScorecardDisplay(Summary,BatCard1)
 print(f"|   TOTAL :-   {inning_total[0]["total"]}/{inning_total[0]["wickets"]}    | ")  
 input()
 print("|                  BOWLING                           ")
 ScorecardDisplay(Summary,BowlCard1)    
 input()
 
 print(f"|             Inning 2 -- {Inning2}                 ")
 
 ScorecardDisplay(Summary,BatCard2)    
 print(f"|   TOTAL :-   {inning_total[1]["total"]}/{inning_total[1]["wickets"]}    | ")  
 input()
 print("|                  BOWLING                           ")
 ScorecardDisplay(Summary,BowlCard2)    
 input()
 print()
 MatchInfo(2,winner,result,toss,toss_sel,man_of_match,series,match_num)
 
# ========   Final -- Calling   =============
def Feature1call():
    # --- Match selection + data loading (moved here from the top level) ---
    output    = FinalCall(3)
    FileName  = output ["filename"]
    Match     = LoadingData(FileName)

    # =========== MATCH-DATA ===========
    info         =  Match["info"]    # === MAIN-INFO (var)

    event        =  info .get("event", {})
    series       =  event.get("name" , "Unkown")
    match_num    =  event.get("match_number" , "Unkown")
    teams        = info["teams"]          
    innings      = Match["innings"]

    while True:    
        outcome      = info["outcome"]  
        if outcome.get("winner"):
            winner       = outcome["winner"]
            result       = outcome["by"]
            toss         = info["toss"]["winner"]
            toss_sel     = info["toss"]["decision"]
            man_of_match = info["player_of_match"][0]
        
        elif outcome.get("result"):
            if outcome['result'] == "no result":
                print(f"Match Result: {outcome['result']} Due to dificult weather")
                break
                 
        BatFirst   = MatchToss(toss,toss_sel,teams)        
        Scorecards = MatchInning(innings)
        EconomySrCalculate(Scorecards)
        Summary    = ScoreCardSepration(Scorecards,info,teams)
        InningDislpay(Summary,Scorecards[2],BatFirst,winner,result,toss,toss_sel,man_of_match,teams,series,match_num)
        break

# Runs only when this file is launched directly (python Main_F1.py),
# NOT when the launcher imports it.
if __name__ == "__main__":
    Feature1call()

