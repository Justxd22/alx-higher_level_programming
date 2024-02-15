-- avg
SELECT city, AVG(value) AS t FROM temperatures GROUP BY city ORDER BY t DESC;