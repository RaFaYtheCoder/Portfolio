import pandas as pd
import time,os

directory   = r"Portfolio\Cricket Stat Engine\Processed Stat\Staduim Stats\stadium_stats.csv"
DataVenue   = pd.read_csv( directory , index_col="Venue" )
data        = pd.read_csv( directory  )
country     = []

def DisplayStat(team):
    output = DataVenue[DataVenue['Country'] == team] 
    print(output)


nation_list = data["Country"]
for team in nation_list:
    if team not in country:    
        country.append(team)
while True:
    print("Nation List :-")
    print("-"*50)

    country = sorted(country)
    for index,value in enumerate(country):
        print(f"{index+1:>3}. {value}")        

    sel = int(input("Your selection: "))

    if sel <= len(country) and sel >= 1:
        sel = sel - 1
        sel_team = country[sel]
        DisplayStat(sel_team)
        break
    
    else:
        print()
        print("-"*50)
        print("Please Select from Index")    




