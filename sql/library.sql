/*
This is SQL code for creating a library database
on a MYSQL Server
*/

/*
SET GLOBAL validate_password_policy=LOW;
SET GLOBAL validate_password_length=5;
SET GLOBAL max_user_connections=1;
*/

CREATE DATABASE library;
USE library;

-- entity tables

CREATE TABLE items (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	loanable ENUM('Y','N') NOT NULL,
	itemType ENUM('BOOK','MAGAZINE','MOVIE','MUSIC'),
	PRIMARY KEY (id) 
);

CREATE TABLE prints (
	itemId SMALLINT UNSIGNED NOT NULL,
	title VARCHAR(255),
	author VARCHAR(255),
	num_pages INT,
	publisher VARCHAR(255),
	year_published YEAR(4),
	language VARCHAR(255),
	isbn_10 CHAR(10),
	isbn_13 CHAR(14),
	PRIMARY KEY (itemId),
	FOREIGN KEY(itemId) REFERENCES items(id) ON DELETE CASCADE
);

CREATE TABLE medias (
	itemId SMALLINT UNSIGNED NOT NULL,
	mediaType VARCHAR(255),
	title VARCHAR(255),
	release_date DATE,
	artist VARCHAR(255),
	label VARCHAR(255),
	asin CHAR(10),
	director VARCHAR(255),
	producer VARCHAR(255),
	actors TEXT,
	languages VARCHAR(255),
	subtitles VARCHAR(255),
	dubbed VARCHAR(255),
	runtime SMALLINT UNSIGNED, -- in minutes
	PRIMARY KEY (itemId),
	FOREIGN KEY(itemId) REFERENCES items(id) ON DELETE CASCADE
);

CREATE TABLE users (
	firstName VARCHAR(255) NOT NULL,
	lastName VARCHAR(255) NOT NULL,
	address VARCHAR(255),
	email VARCHAR(255) NOT NULL,
	pswd VARCHAR(255) NOT NULL,
	phone VARCHAR(20),
	privilegeLevel ENUM('CLIENT','ADMIN') NOT NULL DEFAULT 'CLIENT',
	PRIMARY KEY (email)
);

-- relationship tables

CREATE TABLE loans (
	clientId VARCHAR(255) NOT NULL,
	itemId SMALLINT UNSIGNED NOT NULL,
	loan_date DATE NOT NULL,
	PRIMARY KEY(itemId),
	FOREIGN KEY(clientId) REFERENCES users(email) ON DELETE CASCADE,
	FOREIGN KEY(itemId) REFERENCES items(id) ON DELETE CASCADE
);

-- hardcoded admin

CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin'; -- username = admin / password = admin
GRANT ALL PRIVILEGES ON library.* TO 'admin'@'localhost'
	WITH GRANT OPTION;
    
INSERT INTO users VALUES ('Joshua', 'Butler', NULL, 'admin@localhost', '21232f297a57a5a743894a0e4a801fc3', NULL, 'ADMIN');
