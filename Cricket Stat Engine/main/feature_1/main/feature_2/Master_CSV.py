import pandas as pd
import os

csv_dir = r"Data\CSV Files\Player Stats\Country Vise"
output_file = r"Data\CSV Files\Player Stats\Master.csv"

def CreateMasterCSV(csv_dir, output_file):

    country_map = {
        "PAK": "Pakistan",
        "IND": "India",
        "AUS": "Australia",
        "ENG": "England",
        "NZ": "New Zealand",
        "SA": "South Africa",
        "BAN": "Bangladesh",
        "SRI": "Sri Lanka"
    }

    all_data = []

    for file in os.listdir(csv_dir):

        if file.endswith(".csv"):

            filepath = os.path.join(csv_dir, file)

            data = pd.read_csv(filepath)

            # Add country column from filename
            code = os.path.splitext(file)[0]
            data["Country"] = country_map.get(code, "Unknown")

            all_data.append(data)

    # Merge all country CSVs
    master = pd.concat(all_data, ignore_index=True)

    # Put Country after Player
    columns = master.columns.tolist()

    columns.remove("Country")
    player_index = columns.index("Player")
    columns.insert(player_index + 1, "Country")

    master = master[columns]

    # Sort by Rating

    # Save Master CSV
    master.to_csv(output_file, index=False)

    print("Master CSV Created Successfully!")

CreateMasterCSV(csv_dir, output_file)