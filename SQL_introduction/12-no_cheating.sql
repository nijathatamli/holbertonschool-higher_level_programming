-- that updates the score of Bob to 10 in the table second_table.
SELECT score, name FROM second_table
WHERE 10 =< score
ORDER BY score DESC;