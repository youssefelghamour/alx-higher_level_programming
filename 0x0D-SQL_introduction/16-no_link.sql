-- lists all records of the table second_table
-- doen’t list rows without a name value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
