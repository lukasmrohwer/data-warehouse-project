-- 1. Load Bookings (Note: We set the date style first so it understands 6-28-2022)
SET datestyle = 'SQL, MDY';
COPY fact_booking 
FROM '/tmp/data-warehouse-project/fact_booking.csv' 
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