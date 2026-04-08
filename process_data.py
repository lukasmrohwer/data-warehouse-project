with open("airports.csv", "r") as f:
    airports_lines = f.readlines()

with open("bookings.csv", "r") as f:
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
    #read booking
    passenger_id, fname, lname, gender, age, nationality, airport_name, airport_country_code, country_name, airport_continent, continent, departure_date, arrival_airport, pilot_name, flight_status = line.strip().split(",")
    
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
        fname, lname = pilot_name.split(" ")
        fact_pilot.append([pilot_id, fname, lname])



    dim_booking.append([i, passenger_id, arrival_airport, pilot_id, flight_status])

    i += 1
