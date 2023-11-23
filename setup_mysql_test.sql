-- Create database named 'hbnb_test_db'
-- Create new user called 'hbnb_test' in localhost
-- Set password of new user to 'hbnb_test_pwd'
-- Grant all privileges to new user on this database
-- Grant SELECT privileges to new user to 'perfomance_schema'
-- Flush privileges



-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

--Add new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to new user on this database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';;

-- Flush privileges
FLUSH PRIVILEGES;
