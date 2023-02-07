SET SQL_SAFE_UPDATES = 0;


SELECT * FROM concert_reservation_schema.users;

-- DELETE a record
-- DELETE FROM table_name WHERE condition;
DELETE FROM users
WHERE first_name LIKE '%m';


-- fetch users names and the length of their last name

SELECT id, first_name, last_name, LENGTH(last_name) as name_length
FROM users;

-- concat first_name and email
select id, CONCAT_WS('*',id, first_name, handle) as nmail 
from users;