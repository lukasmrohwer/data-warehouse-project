CREATE TABLE fact_booking (
    BookingID INTEGER PRIMARY KEY,
    PassengerID VARCHAR(50) REFERENCES fact_passenger(PassengerID),
    IATA VARCHAR(10) REFERENCES fact_airport(IATA),
    PilotID INTEGER REFERENCES fact_pilot(PilotID),
    FlightStatus VARCHAR(50),
    DepartureDate DATE
);

CREATE TABLE dim_airport (
    IATA VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(255),
    Municipality VARCHAR(255),
    Region VARCHAR(100),
    Country VARCHAR(100),
    Continent VARCHAR(100),
    Latitude DECIMAL(12, 9),
    Longitude DECIMAL(12, 9),
    Elevation INTEGER,
    Type VARCHAR(50)
);

CREATE TABLE dim_passenger (
    PassengerID VARCHAR(50) PRIMARY KEY,
    FName VARCHAR(100),
    LName VARCHAR(100),
    Gender VARCHAR(20),
    Age INTEGER,
    Nationality VARCHAR(100)
);

CREATE TABLE dim_pilot (
    PilotID INTEGER PRIMARY KEY,
    FName VARCHAR(100),
    LName VARCHAR(100)
);