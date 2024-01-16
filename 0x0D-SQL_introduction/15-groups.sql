-- lists the number of records with the same score in the table second_table
-- displays the score & the number of records for this score with the label number ordered by the number of records (descending)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
