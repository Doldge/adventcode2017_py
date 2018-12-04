CREATE EXTENSION file_fdw;

CREATE SERVER local_storage FOREIGN DATA WRAPPER file_fdw;
DROP FOREIGN TABLE day1_input;
CREATE FOREIGN TABLE day1_input (line_item TEXT NOT NULL)
    SERVER local_storage
    OPTIONS (filename '/home/callum/work/advent_of_code/2018/day1/advent_2018_day_1_pt1_input.txt');

-- Part 1
SELECT sum(line_item::INT) FROM day1_input;


BEGIN;
-- Part 2.
CREATE TEMP TABLE day1_part2 (
	line_sum BIGINT UNIQUE
);

WITH RECURSIVE
	recurse_line_items(line_sum, row_pos) AS (
		SELECT
			0,
			0
		UNION ALL
		SELECT
			line_sum + line_item,
			CASE WHEN row_pos = 954 THEN 0 ELSE row_pos + 1 END as row_pos
		FROM
			recurse_line_items
		LEFT JOIN
			(
				SELECT
					line_item::INT,
					row_number() OVER () as row_id
				FROM day1_input
				ORDER BY row_id ASC
			) as day1
			ON (
				(recurse_line_items.row_pos <= 954 AND (recurse_line_items.row_pos+1) = day1.row_id) OR
				(recurse_line_items.row_pos = 0 AND day1.row_id=1)
			)
	)
INSERT INTO
	day1_part2 (line_sum)
SELECT
	line_sum
FROM
	recurse_line_items
LIMIT 300000;
-- Excepts on your duplicate value.
ABORT;
