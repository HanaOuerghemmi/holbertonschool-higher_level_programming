--  lists the number of records with the same score in the table 
SELECT SUM(score) as number
FROM second_table
ORDER BY score DESC;

