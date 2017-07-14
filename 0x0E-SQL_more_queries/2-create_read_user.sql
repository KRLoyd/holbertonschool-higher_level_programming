-- Create database hbtn_0d_2, if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user_od_2, if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- Set password for the user
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
-- Grant all permissions for *.* user_0d_2
GRANT ALL ON *.* TO 'user_0d_2'@'localhost';
-- Grant SELECT permission for database hbtn_0d_2 for user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
