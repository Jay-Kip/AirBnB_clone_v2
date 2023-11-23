-- Create Database called 'hbnb_dev_db'
-- Create new user  called 'hbnd_dev' in localhost
-- Set password to the new user to 'hbnb_dev_pwd'
-- Grant all privileges to 'hbnb_dev' on database 'hbnb_dev_db'
-- Grant SELECT privileges to 'hbnb_dev' on database schema 'performance schema'
-- Flush Privileges


-- Create Database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Add new user
CREATE USER  IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privileges
GRANT SELECT ON perfomance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes immediately
FLUSH PRIVILEGES;
