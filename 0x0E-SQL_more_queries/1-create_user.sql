-- creates the MySQL server user user_0d_1 with all the privileges and the password user_0d_1_pwd
-- If the user user_0d_1 already exists, the script doesn't fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
