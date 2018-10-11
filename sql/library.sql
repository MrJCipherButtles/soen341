/*
This is SQL code for creating a library database
on a MYSQL Server
*/

SET GLOBAL validate_password_policy=LOW;
SET GLOBAL validate_password_length=5;
SET GLOBAL max_user_connections=1;

CREATE DATABASE library;
USE library;

-- hardcoded admin

CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin'; -- username = admin / password = admin
GRANT ALL PRIVILEGES ON library.* TO 'admin'@'localhost'
	WITH GRANT OPTION;

-- entity tables

CREATE TABLE books (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title VARCHAR(255),
	author VARCHAR(255),
	num_pages INT,
	publisher VARCHAR(255),
	year_published YEAR(4),
	language VARCHAR(255),
	isbn_10 CHAR(10),
	isbn_13 CHAR(14),
	PRIMARY KEY (id)
);

CREATE TABLE magazines (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title VARCHAR(255),
	publisher VARCHAR(255),
	year_published YEAR(4), -- MYSQL YEAR Type
	language VARCHAR(255),
	isbn_10 CHAR(10),
	isbn_13 CHAR(14),
	PRIMARY KEY (id)
);

CREATE TABLE musics (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	type VARCHAR(255),
	title VARCHAR(255),
	release_date DATE,
	artist VARCHAR(255),
	label VARCHAR(255),
	asin CHAR(10),
	PRIMARY KEY (id)
);

CREATE TABLE movies (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title VARCHAR(255),
	director VARCHAR(255),
	producer VARCHAR(255),
	actors TEXT,
	languages VARCHAR(255),
	subtitles VARCHAR(255),
	dubbed VARCHAR(255),
	release_date DATE,
	runtime SMALLINT UNSIGNED, -- in minutes
	PRIMARY KEY (id)
);

CREATE TABLE clients (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	firstName VARCHAR(255) NOT NULL,
	lastName VARCHAR(255) NOT NULL,
	address VARCHAR(255),
	email VARCHAR(255),
	phone VARCHAR(20),
	isAdmin ENUM('TRUE','FALSE') NOT NULL DEFAULT 'FALSE',
	PRIMARY KEY (id)
);

-- relationship tables

CREATE TABLE clients_books (
	clientId SMALLINT UNSIGNED NOT NULL,
	bookId SMALLINT UNSIGNED NOT NULL,
	loan_date DATE NOT NULL,
	due_date DATE,
	return_date DATE,
	PRIMARY KEY(clientId,bookId,loan_date),
	FOREIGN KEY(clientId) REFERENCES clients(id),
	FOREIGN KEY(bookId) REFERENCES books(id)
);

CREATE TABLE clients_magazines (
	clientId SMALLINT UNSIGNED NOT NULL,
	magazineId SMALLINT UNSIGNED NOT NULL,
	loan_date DATE NOT NULL,
	due_date DATE,
	return_date DATE,
	PRIMARY KEY(clientId,magazineId,loan_date),
	FOREIGN KEY(clientId) REFERENCES clients(id),
	FOREIGN KEY(magazineId) REFERENCES magazines(id)
);

CREATE TABLE clients_musics (
	clientId SMALLINT UNSIGNED NOT NULL,
	musicId SMALLINT UNSIGNED NOT NULL,
	loan_date DATE NOT NULL,
	due_date DATE,
	return_date DATE,
	PRIMARY KEY(clientId,musicId,loan_date),
	FOREIGN KEY(clientId) REFERENCES clients(id),
	FOREIGN KEY(musicId) REFERENCES musics(id)
);

CREATE TABLE clients_movies (
	clientId SMALLINT UNSIGNED NOT NULL,
	movieId SMALLINT UNSIGNED NOT NULL,
	loan_date DATE NOT NULL,
	due_date DATE,
	return_date DATE,
	PRIMARY KEY(clientId,movieId,loan_date),
	FOREIGN KEY(clientId) REFERENCES clients(id),
	FOREIGN KEY(movieId) REFERENCES movies(id)
);
