-- show the max temp of each state ordered
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;