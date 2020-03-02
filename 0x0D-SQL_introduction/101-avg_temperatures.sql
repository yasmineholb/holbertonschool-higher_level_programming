-- task 101
SELECT city, AVG(value) AS avg_temp
FROM temperatures
ORDER BY value DESC;
