-- This script prints the full description of the table first_table

SELECT CONCAT('Table: ', table_name, '\nCreate Table: ', create_statement) AS 'Table Description'
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';

