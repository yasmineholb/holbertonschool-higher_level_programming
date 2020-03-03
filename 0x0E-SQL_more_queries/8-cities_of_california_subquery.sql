-- task 8
SELECT *
FROM cities
WHERE states.name = California AND cities.state_id = states.id
ORDER BY cities.id DESC;
