import re

with open("airports.csv", "r", encoding="utf-8") as f:
    airports_lines = f.readlines()

with open("bookings.csv", "r", encoding="utf-8") as f:
    bookings_lines = f.readlines()

fact_passenger = []
fact_airport = []
fact_pilot = []
dim_booking = []

pilots = {}
passengers = set()
airports = {}

i = 0
for line in bookings_lines[1:]:
    #deal with commas in quotes
    line = re.sub(r'"([^",]+)[^"]*"', r'\1', line)

    #read booking
    try:
        passenger_id, fname, lname, gender, age, nationality, airport_name, airport_country_code, country_name, airport_continent, continent, departure_date, arrival_airport, pilot_name, flight_status = line.strip().split(",")
    except ValueError:
        print(f"Skipping line due to parsing error: {line.strip()}")
        break

    if arrival_airport == "-" or arrival_airport == "0":
        continue

    #add passenger data
    if passenger_id not in passengers:
        passengers.add(passenger_id)
        fact_passenger.append([passenger_id, fname, lname, gender, age, nationality])
    
    #add airport data
    # if arrival_airport not in airports:
    #     airports.add(arrival_airport)
    #     fact_airport.append([arrival_airport, airport_name, continent, country_name])
    if arrival_airport not in airports:
        airports[arrival_airport] = {
            "name": airport_name,
            "continent": continent,
            "country_name": country_name
        }

    #add pilot data
    if pilot_name not in pilots:
        pilots[pilot_name] = len(pilots)
        pilot_id = pilots[pilot_name]
        lname = pilot_name.split(" ")[-1]
        fname = " ".join(pilot_name.split(" ")[:-1])
        fact_pilot.append([pilot_id, fname, lname])
    pilot_id = pilots[pilot_name]

    #add booking data
    departure_date = departure_date.replace("/", "-")
    dim_booking.append([i, passenger_id, arrival_airport, pilot_id, flight_status, departure_date])

    i += 1

for line in airports_lines[1:]:
    #deal with commas in quotes
    line = re.sub(r'"([^",]+)[^"]*"', r'\1', line)

    #extract data
    try:
        airport_id,ident,airport_type,name,latitude_deg,longitude_deg,elevation_ft,continent,iso_country,iso_region,municipality,scheduled_service,icao_code,iata_code,gps_code,local_code,home_link,wikipedia_link,keywords = line.strip().split(",")
    except ValueError:
        print(f"Skipping line due to parsing error: {line.strip()}")
        continue

    #add additional data
    if iata_code in airports:
        airports[iata_code]["latitude_deg"] = latitude_deg
        airports[iata_code]["longitude_deg"] = longitude_deg
        airports[iata_code]["elevation_ft"] = elevation_ft
        airports[iata_code]["airport_type"] = airport_type
        airports[iata_code]["municipality"] = municipality
        airports[iata_code]["iso_region"] = iso_region
        continue

    #fallback incase airport data does not include iata code
    for iata_code, data in airports.items():
        if data["name"] == name:
            airports[iata_code]["latitude_deg"] = latitude_deg
            airports[iata_code]["longitude_deg"] = longitude_deg
            airports[iata_code]["elevation_ft"] = elevation_ft
            airports[iata_code]["airport_type"] = airport_type
            airports[iata_code]["municipality"] = municipality
            airports[iata_code]["iso_region"] = iso_region

for iata_code, data in airports.items():
    fact_airport.append([iata_code, data["name"], data.get("municipality", ""), data.get("iso_region", ""), data["country_name"], data["continent"], data.get("latitude_deg", ""), data.get("longitude_deg", ""), data.get("elevation_ft", ""), data.get("airport_type", "")])

#write data to csv files
with open("fact_passenger.csv", "w", encoding="utf-8") as f:
    f.write("PassengerID,FName,LName,Gender,Age,Nationality\n")
    for passenger in fact_passenger:
        f.write(",".join(passenger) + "\n")

with open("fact_airport.csv", "w", encoding="utf-8") as f:
    f.write("IATA,Name,Municipality,Region,Country,Continent,Latitude,Longitude,Elevation,Type\n")
    for airport in fact_airport:
        f.write(",".join(airport) + "\n")

with open("fact_pilot.csv", "w", encoding="utf-8") as f:
    f.write("PilotID,FName,LName\n")
    for pilot in fact_pilot:
        f.write(",".join(map(str, pilot)) + "\n")

with open("dim_booking.csv", "w", encoding="utf-8") as f:
    f.write("BookingID,PassengerID,IATA,PilotID,FlightStatus,DepartureDate\n")
    for booking in dim_booking:
        f.write(",".join(map(str, booking)) + "\n")