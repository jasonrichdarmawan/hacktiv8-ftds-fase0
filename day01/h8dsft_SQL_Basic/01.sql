-- list possible subscriber_type: Subscriber, Customer
-- SELECT DISTINCT a.subscriber_type
-- FROM bigquery-public-data.san_francisco.bikeshare_trips AS a
-- LIMIT 10;

-- list possible landmark: Redwood City
-- SELECT DISTINCT b.landmark
-- FROM bigquery-public-data.san_francisco.bikeshare_stations AS b
-- LIMIT 10;

-- list if the query is valid
-- SELECT 
-- a.trip_id, a.start_date, a.subscriber_type, a.start_station_name, a.start_station_id,
-- b.station_id, b.name, b.landmark
-- FROM bigquery-public-data.san_francisco.bikeshare_trips AS a
-- LEFT JOIN bigquery-public-data.san_francisco.bikeshare_stations AS b
-- ON a.start_station_id = b.station_id
-- WHERE a.start_date BETWEEN '2016-01-01' AND '2016-03-31'
-- AND a.subscriber_type = "Subscriber"
-- AND b.landmark LIKE "Redwood City"
-- LIMIT 10;

-- Query 1: Count Q1
SELECT COUNT(a.trip_id) AS entry
FROM bigquery-public-data.san_francisco.bikeshare_trips AS a
LEFT JOIN bigquery-public-data.san_francisco.bikeshare_stations AS b
ON a.start_station_id = b.station_id
WHERE a.start_date BETWEEN '2016-01-01' AND '2016-03-31'
AND a.subscriber_type = "Subscriber"
AND b.landmark LIKE "Redwood City";

-- Query 2: Count Q2
SELECT COUNT(a.trip_id) AS entry
FROM bigquery-public-data.san_francisco.bikeshare_trips AS a
LEFT JOIN bigquery-public-data.san_francisco.bikeshare_stations AS b
ON a.start_station_id = b.station_id
WHERE a.start_date BETWEEN '2016-04-01' AND '2016-06-30'
AND a.subscriber_type = "Subscriber"
AND b.landmark LIKE "Redwood City";

-- Out-of-scope: In 1 Query
-- SELECT 
-- COUNT(CASE WHEN a.start_date BETWEEN '2016-01-01' AND '2016-03-31' THEN 1 END) AS Q1,
-- COUNT(CASE WHEN a.start_date BETWEEN '2016-04-01' AND '2016-06-30' THEN 1 END) AS Q2
-- FROM bigquery-public-data.san_francisco.bikeshare_trips AS a
-- LEFT JOIN bigquery-public-data.san_francisco.bikeshare_stations AS b
-- ON a.start_station_id = b.station_id
-- WHERE a.subscriber_type = "Subscriber"
-- AND b.landmark LIKE "Redwood City";