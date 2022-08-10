-- Script that creates table `unique_id` with  a default unique id of 1 on MySQl server
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
