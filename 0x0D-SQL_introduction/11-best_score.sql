-- Lists all records in the table second_table with a score >= 10.
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` > 9
ORDER BY `score` DESC;
