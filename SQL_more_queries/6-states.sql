-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE states(
	id INT NOT NULL AUTO_INCREMENT UNIQUE,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id) 
)
