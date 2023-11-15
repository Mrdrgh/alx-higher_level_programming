-- create a table with a default value for a column
CREATE TABLE IF NOT EXISTS id_not_null (
    id INTEGER DEFAULT 1,
    name VARCHAR(256)
);