-- Script to create MySQL server user user_0d_1 and set permissions
-- Create user_0d_1 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- Set the password for the user
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';
-- Set permissions for user_0d_1
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
