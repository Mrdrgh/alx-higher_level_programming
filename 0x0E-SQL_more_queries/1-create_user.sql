-- create user and grant all privileges even if existing already
CREATE USER IF NOT EXISTS user_0d_1@locathost IDENTIFIED BY
'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;