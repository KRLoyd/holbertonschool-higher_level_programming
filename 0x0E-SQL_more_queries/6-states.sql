-- Create database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Specify we want to use hbtn_0d_usa
USE hbtn_0d_usa;
-- Create table hbtn_0d_usa in database hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
