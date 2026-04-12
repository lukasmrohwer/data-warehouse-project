DROP TABLE IF EXISTS fact_booking;
DROP TABLE IF EXISTS dim_airport;
DROP TABLE IF EXISTS dim_passenger;
DROP TABLE IF EXISTS dim_pilot;

-- Create Dimension Tables First (so Foreign Keys have a target to reference)

CREATE TABLE dim_airport (
    IATA VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(255),
    Type VARCHAR(50),
    Continent VARCHAR(100),
    Country VARCHAR(100),
    Region VARCHAR(100),
    Municipality VARCHAR(255),
    Latitude DECIMAL(12, 9),
    Longitude DECIMAL(12, 9),
    Elevation DECIMAL(10, 2)
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

-- Create Fact Table Last

CREATE TABLE fact_booking (
    BookingID INTEGER PRIMARY KEY,
    PassengerID VARCHAR(50) REFERENCES dim_passenger(PassengerID),
    IATA VARCHAR(10) REFERENCES dim_airport(IATA),
    PilotID INTEGER REFERENCES dim_pilot(PilotID),
    FlightStatus VARCHAR(50),
    DepartureDate DATE
);