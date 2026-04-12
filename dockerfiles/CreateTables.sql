DROP TABLE IF EXISTS fact_booking CASCADE;
DROP TABLE IF EXISTS dim_airport CASCADE;
DROP TABLE IF EXISTS dim_country CASCADE;
DROP TABLE IF EXISTS dim_passenger CASCADE;
DROP TABLE IF EXISTS dim_pilot CASCADE;

-- Create Dimension Tables First

-- 1. Create the new Country dimension
CREATE TABLE dim_country (
    country_name VARCHAR(100) PRIMARY KEY,
    avg_precipitation_mm NUMERIC,
    co2_emissions_pc NUMERIC,
    gdp_usd NUMERIC,
    gdp_per_capita_usd NUMERIC,
    total_population BIGINT
);

-- 2. Create Airport (Now referencing dim_country)
CREATE TABLE dim_airport (
    IATA VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(255),
    Type VARCHAR(50),
    Continent VARCHAR(100),
    Country VARCHAR(100) REFERENCES dim_country(country_name),
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


-- Load Data (Dimensions first, then Facts)

-- 1. Load Countries (Must be loaded before airports so the Foreign Key works!)
COPY dim_country 
FROM '/tmp/data-warehouse-project/dim_country.csv' 
DELIMITER ',' CSV HEADER;

-- 2. Load Airports
COPY dim_airport 
FROM '/tmp/data-warehouse-project/dim_airport.csv' 
DELIMITER ',' CSV HEADER;

-- 3. Load Passengers
COPY dim_passenger 
FROM '/tmp/data-warehouse-project/dim_passenger.csv' 
DELIMITER ',' CSV HEADER;

-- 4. Load Pilots
COPY dim_pilot 
FROM '/tmp/data-warehouse-project/dim_pilot.csv' 
DELIMITER ',' CSV HEADER;

-- 5. Load Bookings
SET datestyle = 'SQL, MDY';
COPY fact_booking 
FROM '/tmp/data-warehouse-project/fact_booking.csv' 
DELIMITER ',' CSV HEADER;