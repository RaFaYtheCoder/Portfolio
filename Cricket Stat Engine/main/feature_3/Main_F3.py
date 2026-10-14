import pandas as pd
import time,os

directory   = r"Portfolio\Cricket Stat Engine\Processed Stat\Staduim Stats\stadium_stats.csv"

def DisplayStat(DataVenue,team):
    output = DataVenue[DataVenue['Country'] == team] 
    print(output)


def Feature3_Calling():
    # --- Loading moved here from the top level ---
    try:
        DataVenue   = pd.read_csv( directory , index_col="Venue" )
        nation_list = DataVenue["Country"].dropna()

    except FileNotFoundError:
        print(f"Stadium CSV not found at: {directory}")
        return

    except (ValueError, pd.errors.EmptyDataError):
        print("Stadium CSV is empty or has no 'Venue' column.")
        return

    except KeyError:
        print("Stadium CSV has no 'Country' column.")
        return

    country     = []

    for team in nation_list:
        if team not in country:    
            country.append(team)
    while True:
        print("Nation List :-")
        print("-"*50)

        country = sorted(country)
        for index,value in enumerate(country):
            print(f"{index+1:>3}. {value}")        

        try:
            sel = int(input("Your selection: "))
        except ValueError:
            print()
            print("-"*50)
            print("Please enter a number")
            continue

        if sel <= len(country) and sel >= 1:
            sel = sel - 1
            sel_team = country[sel]
            DisplayStat(DataVenue,sel_team)
            break
        
        else:
            print()
            print("-"*50)
            print("Please Select from Index")    

# Runs only when this file is launched directly (python Main_F3.py),
# NOT when the launcher imports it.
if __name__ == "__main__":
    Feature3_Calling()
