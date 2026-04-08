-- 1. Load Bookings (Note: We set the date style first so it understands 6-28-2022)
SET datestyle = 'SQL, MDY';
COPY dim_booking 
FROM '/tmp/data-warehouse-project/dim_booking.csv' 
DELIMITER ',' CSV HEADER;

-- 2. Load Airports
COPY fact_airport 
FROM '/tmp/data-warehouse-project/fact_airport.csv' 
DELIMITER ',' CSV HEADER;

-- 3. Load Passengers
COPY fact_passenger 
FROM '/tmp/data-warehouse-project/fact_passenger.csv' 
DELIMITER ',' CSV HEADER;

-- 4. Load Pilots
COPY fact_pilot 
FROM '/tmp/data-warehouse-project/fact_pilot.csv' 
DELIMITER ',' CSV HEADER;