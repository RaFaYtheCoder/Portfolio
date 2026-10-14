import csv
import requests

API_KEY = "fee1ac8be37a4daeaf033282611ee75b"
CSV_FILE = r"Data\CSV Files\Staduim Stats\stadium_stats.csv"


def CountryGetter(venue, city):

    url = "https://api.geoapify.com/v1/geocode/search"

    params = {
        "text": f"{venue}, {city}",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["features"]:

        properties = data["features"][0]["properties"]
        rank = properties.get("rank", {})

        confidence = rank.get("confidence", 0)
        confidence_city = rank.get("confidence_city_level", 0)
        confidence_building = rank.get("confidence_building_level", 0)
        match_type = rank.get("match_type", "Unknown")

        country = properties.get("country", "Unknown")

        print(
            f"{venue}, {city} → {country}"
            f" | Confidence: {confidence}"
            f" | City: {confidence_city}"
            f" | Building: {confidence_building}"
            f" | Match: {match_type}"
        )

        return country

    return "Unknown"


def UpdateCSV():

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    for row in rows:

        venue = row["Venue"]
        city = row["City"]

        if city == "0" or city == "Unknown":
            continue

        country = CountryGetter(venue, city)
        row["Country"] = country

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:

        fieldnames = rows[0].keys()

        writer = csv.DictWriter(
            f,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(rows)


UpdateCSV()