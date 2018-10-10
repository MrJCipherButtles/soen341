/*
This is SQL code for creating a library database
on a MYSQL Server
*/

CREATE DATABASE library;
USE library;

-- hardcoded admin

-- CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin'; -- username = admin / password = admin
-- GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';

-- entity tables

CREATE TABLE books (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title VARCHAR(100),
	author VARCHAR(100),
	num_pages INT,
	publisher VARCHAR(100),
	year_published YEAR(4),
	language VARCHAR(100),
	isbn_10 CHAR(10),
	isbn_13 CHAR(14),
	PRIMARY KEY (id)
);

CREATE TABLE magazines (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title VARCHAR(100),
	publisher VARCHAR(100),
	year_published YEAR(4), -- MYSQL YEAR Type
	language VARCHAR(100),
	isbn_10 CHAR(10),
	isbn_13 CHAR(14),
	PRIMARY KEY (id)
);

CREATE TABLE musics (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	type VARCHAR(100),
	title VARCHAR(100),
	release_date DATE,
	artist VARCHAR(100),
	label VARCHAR(100),
	asin CHAR(10),
	PRIMARY KEY (id)
);

CREATE TABLE movies (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title VARCHAR(100),
	director VARCHAR(100),
	producer VARCHAR(100),
	actors TEXT,
	languages VARCHAR(100),
	subtitles VARCHAR(100),
	dubbed VARCHAR(100),
	release_date DATE,
	runtime SMALLINT UNSIGNED, -- in minutes
	PRIMARY KEY (id)
);

CREATE TABLE clients (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	firstName VARCHAR(100) NOT NULL,
	lastName VARCHAR(100) NOT NULL,
	address VARCHAR(100),
	email VARCHAR(100),
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
