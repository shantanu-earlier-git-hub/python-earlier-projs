 CREATE USER 'dbuser' IDENTIFIED BY 'passw0rd';

GRANT ALL PRIVILEGES ON *.* TO 'dbuser' WITH GRANT OPTION;


flush privileges;
