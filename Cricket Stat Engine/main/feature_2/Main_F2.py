import pandas   as pd
import os,time,operator

# Player, Country , Role , Matches , MOTM,
# Runs  , Balls  , Outs , Batting Avg, 100s, 50s , Highest Score, Strike Rate,
# Wickets, Economy, Bowling Avg, Runs Conceded, Balls Bowled, Rating

master_file = r"Portfolio\Cricket Stat Engine\Processed Stat\Player Stats\Master.csv"

# -----------------| GET STATS |-----------------

def StatsGetter(Data):
    MainLoop = True
    stored_stats = []
    headings = list(Data.columns)
    
    headings.remove("Country")    
    headings.remove("Role")

    while MainLoop:

        # Display all headings
        for index, stat in enumerate(headings, start=1):
            print(f"{index:<2}. {stat:<19}|", end="")
            if index % 3 == 0:
                print()
        print()
        print("-" * 50)

        # ----- Input Validation -----
        while True:
            try:
                index_sel = int(input("Selection : "))
                break
            except ValueError:
                print("Invalid Input !!! Please Select Again from the given index")
                print("=" * 40)

        heading_size = len(headings)

        # ----- Valid Index -----
        if 1 <= index_sel <= heading_size:

            selected_stat = headings[index_sel - 1]

            print("=" * 50)
            print(f"You have selected {selected_stat}")
            print("-" * 50)

            stored_stats.append(selected_stat)

            while True:

                Yes_NO = input(
                    "Do You Wanted to Add another stat as condition (Y/N) : "
                ).lower()

                if Yes_NO == "y":

                    headings.remove(selected_stat)
                    os.system("cls")
                    break

                elif Yes_NO == "n":

                    print("\nYou Have selected These Stats :-")
                    print("-" * 40)

                    for count, selection in enumerate(stored_stats, start=1):
                        print(f"{count}. {selection}")

                    time.sleep(2)

                    MainLoop = False
                    break

                else:

                    print()
                    print("Press (Y) for Yes | (N) for No")
                    print("-" * 50)

        # ----- Invalid Index -----
        else:

            print()
            print(f"Invalid Index. Select between (1-{heading_size})")
            print("-" * 50)
            input("Press Enter to Continue...")
            os.system("cls")

    return stored_stats

# -----------------| GET OPERATORS & VALUES |-----------------

def ConditionAssigner(Stats):
    GivenData = {}
    operators = [">", "<", ">=", "<=", "=="]
    os.system("cls")

    print("Assign Conditions to the Selected Stats")
    print("-" * 50)
    for count, stat in enumerate(Stats, start=1):
        # ----- Number -----
        while True:
            try:
                print("-" * 50)
                num_given = float(input(f"{count}. {stat} : "))
                break
            except ValueError:
                print("Expected Integer or Float !!!")
                time.sleep(1)
                os.system("cls")

        # ----- Operator -----
        for index,op in enumerate(operators , start=1):
                print(f"{index}. {op}  | ",end="")
        while True:
            try:
                sel_symbol = int(input("Selection (Index): "))

                # 0 or a negative number would silently pick from the end of the list
                if sel_symbol < 1 or sel_symbol > len(operators):
                    raise IndexError

                symbol = operators[sel_symbol-1]
                break

            except ValueError:
                print("Please enter a number.")

            except IndexError:
                print("Please select from the given index.")
        
        # ----- Store -----
        GivenData[stat] = {
            "operator": symbol,
            "number": num_given
        }

    return GivenData

def ConditionMaker(Data,conditional_item):
    matches = False 
    ops = { ">" : operator.gt,
            "<" : operator.lt,
            ">=": operator.ge,
            "<=": operator.le,
            "==": operator.eq,
            "!=": operator.ne }
    
    conditon       = 0          
    condition_stat = []

    for index,(stat,value) in enumerate(conditional_item.items(), start=1):
        symbol          = value["operator"] 
        number          = value["number"]        

        condition_stat.append(stat)
        
        if index == 1:
            conditon = ops[symbol](Data[stat] , number )
        else:
            conditon = conditon & ops[symbol](Data[stat] , number )

        # Players with no wickets have a Bowling Avg of inf - leave them out
        if stat == "Bowling Avg":
            conditon = conditon & (Data[stat] != float("inf"))

        if stat == "Matches":
            matches = True   
        
    
    result = Data[conditon]

    if matches :
        defualt_stat   =  ["Country" , "Role" , "Rating"] 
    else:
        defualt_stat   =  ["Country" , "Role" , "Matches" , "Rating" ] 
    
    # Don't show a column twice (e.g. when Rating is also a condition)
    extra_stat = []
    for s in condition_stat:
        if s not in defualt_stat:
            extra_stat.append(s)

    FinalOutput = result[defualt_stat + extra_stat]
    print(FinalOutput)

                                        
def Feature2_Calling():
    # --- Loading moved here from the top level ---
    try:
        master_data = pd.read_csv(master_file , index_col="Player")

    except FileNotFoundError:
        print(f"Master CSV not found at: {master_file}")
        return

    except (ValueError, pd.errors.EmptyDataError):
        print("Master CSV is empty or has no 'Player' column.")
        return

    try:
        stats     = StatsGetter(master_data)
        GivenData = ConditionAssigner(stats)
        ConditionMaker(master_data,GivenData)

    except KeyError as missing:
        print(f"Column not found in the data: {missing}")

    except ValueError:
        print("Master CSV must contain 'Country' and 'Role' columns.")

# Runs only when this file is launched directly (python Main_F2.py),
# NOT when the launcher imports it.
if __name__ == "__main__":
    Feature2_Calling()
