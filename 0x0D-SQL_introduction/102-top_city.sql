-- avg
SELECT city, AVG(value) AS t FROM (SELECT city, month, value FROM temperatures WHERE month=7 OR month=8) AS A
GROUP BY city ORDER BY t DESC LIMIT 3;