/*
This is SQL code for creating a library database
on a MYSQL Server
*/

CREATE DATABASE library;
USE library;

-- entity tables

CREATE TABLE books (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title VARCHAR(50),
	author VARCHAR(50),
	num_pages INT,
	publisher VARCHAR(50),
	year_published INT,
	language VARCHAR(50),
	isbn_10 CHAR(10),
	isbn_13 CHAR(13),
	PRIMARY KEY (id)
);

CREATE TABLE magazines (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title VARCHAR(50),
	publisher VARCHAR(50),
	year_published YEAR(4), -- MYSQL YEAR Type
	language VARCHAR(50),
	isbn_10 CHAR(10),
	isbn_13 CHAR(13),
	PRIMARY KEY (id)
);

CREATE TABLE musics (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	type VARCHAR(50),
	title VARCHAR(50),
	release_date DATE,
	artist VARCHAR(50),
	label VARCHAR(50),
	asin CHAR(10),
	PRIMARY KEY (id)
);

CREATE TABLE movies (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	title VARCHAR(50),
	director VARCHAR(50),
	producer VARCHAR(50),
	actors TEXT,
	languages VARCHAR(50),
	subtitles VARCHAR(50),
	dubbed VARCHAR(50),
	release_date DATE,
	runtime SMALLINT UNSIGNED, -- in minutes
	PRIMARY KEY (id)
);

CREATE TABLE clients (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	firstName VARCHAR(50) NOT NULL,
	lastName VARCHAR(50) NOT NULL,
	addresse VARCHAR(100),
	email VARCHAR(50),
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