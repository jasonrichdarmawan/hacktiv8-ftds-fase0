# Start the MySQL Server

```
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d -p 3306:3306/tcp mysql:8.0
```

# dataset 1

https://drive.google.com/file/d/1Ur_5ZuWxl8Rr00o-HSDwIQvxDqIeRGif/view?usp=sharing

```
SELECT * 
 FROM hacktiv8.aapl_historical_stock_price;

SELECT COUNT(*)
 FROM hacktiv8.aapl_historical_stock_price;
  
SELECT COUNT(high)
 FROM hacktiv8.aapl_historical_stock_price;
  
SELECT SUM(volume) AS total_volume
 FROM hacktiv8.aapl_historical_stock_price;

SELECT AVG(high)
 FROM hacktiv8.aapl_historical_stock_price
 WHERE high IS NOT NULL;

SELECT AVG(high)
 FROM hacktiv8.aapl_historical_stock_price;

SELECT year,
	   month,
       COUNT(*) AS count
 FROM hacktiv8.aapl_historical_stock_price
 GROUP BY year, month
 ORDER BY year, month;

SELECT year,
       month,
       MAX(high) AS month_high
 FROM hacktiv8.aapl_historical_stock_price
 GROUP BY year, month
  # column that was aggregated with GROUP BY / 
  # aggregated column with function e.g AVG(high)
  HAVING MAX(high) > 400 AND AVG(high) > 400 AND year = 2011
 ORDER BY year, month;

SELECT close,
       CASE 
        WHEN close > 500 THEN 'yes'
		ELSE 'no' 
	   END AS big_number
 FROM hacktiv8.aapl_historical_stock_price;

SELECT close,
       CASE
        WHEN close > 500 THEN 'yes'
        WHEN close > 300 THEN 'maybe'
        ELSE 'no'
	   END AS big_number
 FROM hacktiv8.aapl_historical_stock_price;

SELECT DISTINCT year, month
 FROM hacktiv8.aapl_historical_stock_price;

SELECT COUNT(DISTINCT month) AS unique_months
 FROM hacktiv8.aapl_historical_stock_price;
 
SELECT *
 FROM (
  SELECT *
   FROM hacktiv8.aapl_historical_stock_price
   WHERE year = 2014
 ) AS aapl_historical_stock_price
WHERE close > 400;
```

# dataset 2

https://drive.google.com/file/d/1dIJugnN9wrSIsHctYl5iROduThcHXsci/view?usp=sharing

```
SELECT *
 FROM hacktiv8.dc_bikeshare_q1_2012;

SELECT start_time,
       duration_seconds,
	   SUM(duration_seconds) OVER (ORDER BY start_time) AS running_total
 FROM hacktiv8.dc_bikeshare_q1_2012;

SELECT start_terminal,
       duration_seconds,
       SUM(duration_seconds) OVER
         (PARTITION BY start_terminal) AS running_total,
       COUNT(duration_seconds) OVER
         (PARTITION BY start_terminal) AS running_count,
       AVG(duration_seconds) OVER
         (PARTITION BY start_terminal) AS running_avg
  FROM hacktiv8.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08';
 
SELECT start_terminal,
       start_time,
       duration_seconds,
       ROW_NUMBER() OVER (ORDER BY start_time) AS rn
 FROM hacktiv8.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08';
 
SELECT start_terminal,
       start_time,
       duration_seconds,
       ROW_NUMBER() OVER (PARTITION BY start_terminal
                          ORDER BY start_time) AS rn
 FROM hacktiv8.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08';
 
SELECT start_terminal,
	   duration_seconds,
       start_time,
       RANK() OVER (PARTITION BY start_terminal
                    ORDER BY start_time) AS ranking
 FROM hacktiv8.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08';
 
SELECT start_terminal,
       duration_seconds,
       NTILE(4) OVER (PARTITION BY start_terminal 
					  ORDER BY duration_seconds) 
				AS quartile,
       NTILE(5) OVER (PARTITION BY start_terminal 
					  ORDER BY duration_seconds)
				AS quantile,
       NTILE(100) OVER (PARTITION BY start_terminal 
						ORDER BY duration_seconds)
				  AS percentile
  FROM hacktiv8.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'
 ORDER BY start_terminal, duration_seconds;
 
SELECT start_terminal,
	   LAG(start_terminal,2) OVER (ORDER BY duration_seconds),
       LEAD(start_terminal,2) OVER (ORDER BY duration_seconds)
  FROM hacktiv8.dc_bikeshare_q1_2012;

SELECT start_terminal,
       duration_seconds,
       duration_seconds - LAG(duration_seconds, 1) OVER (PARTITION BY start_terminal
														 ORDER BY duration_seconds)
												   AS difference
FROM hacktiv8.dc_bikeshare_q1_2012
WHERE start_time < '2012-01-08'
ORDER BY start_terminal, duration_seconds;

SELECT *
FROM (
 SELECT start_terminal,
		duration_seconds,
		duration_seconds - LAG(duration_seconds, 1) OVER (PARTITION BY start_terminal 
														  ORDER BY duration_seconds)
													AS difference
 FROM hacktiv8.dc_bikeshare_q1_2012
 WHERE start_time < '2012-01-08'
 ORDER BY start_terminal, duration_seconds
) sub
WHERE sub.difference IS NOT NULL;
```