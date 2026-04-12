## Starnet Link
https://drive.google.com/file/d/1tV8Ty4mc5T37EY-uexJ1G8NrLtV6BnUj/view?usp=sharing


## Usage

Copy sql commands and data in docker volume.
`docker cp dockerfiles pgdb:/tmp/data-warehouse-project`

Copy the code from the sql files and run them.

Example SQL Query
```
SELECT * FROM fact_booking
JOIN dim_airport ON dim_airport.iata = fact_booking.iata
WHERE dim_airport.iata = 'PER'
```