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
airports = set()

i = 0
for line in bookings_lines[1:]:
    line = re.sub(r'"([^",]+)[^"]*"', r'\1', line)

    #read booking
    try:
        passenger_id, fname, lname, gender, age, nationality, airport_name, airport_country_code, country_name, airport_continent, continent, departure_date, arrival_airport, pilot_name, flight_status = line.strip().split(",")
    except ValueError:
        print(f"Skipping line due to parsing error: {line.strip()}")
        break

    #add passenger data
    if passenger_id not in passengers:
        passengers.add(passenger_id)
        fact_passenger.append([passenger_id, fname, lname, gender, age, nationality])
    
    #add airport data
    if arrival_airport not in airports:
        airports.add(arrival_airport)
        fact_airport.append([arrival_airport, airport_name, country_name, continent])

    if pilot_name not in pilots:
        pilots[pilot_name] = len(pilots)
        pilot_id = pilots[pilot_name]
        lname = pilot_name.split(" ")[-1]
        fname = " ".join(pilot_name.split(" ")[:-1])
        fact_pilot.append([pilot_id, fname, lname])
    pilot_id = pilots[pilot_name]

    dim_booking.append([i, passenger_id, arrival_airport, pilot_id, flight_status])

    i += 1

with open("fact_passenger.csv", "w", encoding="utf-8") as f:
    for passenger in fact_passenger:
        f.write(",".join(passenger) + "\n")

with open("fact_airport.csv", "w", encoding="utf-8") as f:
    for airport in fact_airport:
        f.write(",".join(airport) + "\n")

with open("fact_pilot.csv", "w", encoding="utf-8") as f:
    for pilot in fact_pilot:
        f.write(",".join(map(str, pilot)) + "\n")

with open("dim_booking.csv", "w", encoding="utf-8") as f:
    for booking in dim_booking:
        f.write(",".join(map(str, booking)) + "\n")
