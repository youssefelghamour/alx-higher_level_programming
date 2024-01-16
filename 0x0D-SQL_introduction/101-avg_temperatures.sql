-- displays the average temperature (Fahrenheit) by city from temperatures.sql
-- ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
