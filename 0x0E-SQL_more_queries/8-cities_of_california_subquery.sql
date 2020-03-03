-- task 8
SELECT *
FROM cities, states
WHERE states.name = California
ORDER BY cities.id DESC;
