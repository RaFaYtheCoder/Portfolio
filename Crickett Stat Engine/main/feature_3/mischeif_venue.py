import csv

CSV_FILE = r"Data\CSV Files\Staduim Stats\stadium_stats.csv"

WI_Islands = [
    "Antigua and Barbuda",
    "Bahamas",
    "Barbados",
    "Cuba",
    "Dominica",
    "Dominican Republic",
    "Grenada",
    "Guyana",
    "Haiti",
    "Jamaica",
    "Saint Kitts and Nevis",
    "St. Kitts and Nevis",
    "Saint Lucia",
    "St. Lucia",
    "Saint Vincent and the Grenadines",
    "St. Vincent and the Grenadines",
    "Suriname",
    "Trinidad and Tobago"
]


def ChangeToWestIndies():

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    for row in rows:

        country = row["Country"]

        if country in WI_Islands:

            row["Country"] = "West Indies"

            print(f"{country} → West Indies")

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:

        fieldnames = rows[0].keys()

        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(rows)


ChangeToWestIndies()