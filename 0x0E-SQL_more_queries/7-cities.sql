-- create a db and cities as table with multiple constrains in it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INTEGER NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES state(id)
);