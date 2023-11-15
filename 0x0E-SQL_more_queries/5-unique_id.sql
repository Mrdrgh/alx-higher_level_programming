-- create a table with column with constrainte unique and default
CREATE TABLE IF NOT EXISTS unique_id (
    id INTEGER DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);