-- display top 3 cities temp in july and aug
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;