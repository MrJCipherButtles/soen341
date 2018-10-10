INSERT INTO library.books (title,author,num_pages,publisher,year_published,language,isbn_10,isbn_13)
VALUES
('Grapes of Wrath', 'John Steinbeck', 241, 'Penguin Publishing', 1931, 'English',7593648531,'834-7593648531'),
('Le monde sans Faim', 'George Lecavalier', 53, 'Access Litterature', 1994, 'French', 9301756562, '123-9301756562'),
('People are Animals', 'Jane Joyce', 347, 'Worldwide', 2008, 'English', 9044591234, '892-9044591234');

INSERT INTO library.magazines (title, publisher, year_published, language, isbn_10, isbn_13)
VALUES
('Le Monde', 'Le Monde Publishing', 2005, 'French', 8937293950, '847-8937293950'),
('Cosmopolitan', 'No Name Publishing', 2015, 'English', 5723957738, '920-5723957738'),
('Actuary Weekly', 'CPA', 2004, 'English', 9504762930, '583-9504762930');

INSERT INTO library.musics (type, title, release_date, artist, label, asin)
VALUES
('Vinyl', 'The Reign of Kindo EP', '2011-02-11',  'The Reign of Kindo','Independant', NULL),
('Digital', 'The Mountain', '2013-04-21',  'Haken','Universal', NULL),
('CD', 'Best Of the Commodores', '1990-05-30',  'Commodores','Motown', NULL);

INSERT INTO library.clients (firstname, lastname, address, email, phone, isAdmin)
VALUES
('Justin', 'Malone', '950 real street, Montreal', 'justind.malone@domain.ca','514-514-5145', 'FALSE'),
('Alex', 'Baker', '42 Baker street, Sherbrooke', 'alex.baker1997@domain.ca','514-514-5165', 'FALSE'),
('Alfred', 'Augustus', '5716 Summer boulevard, Quebec City', 'AA@domain.ca','418-385-3893', 'FALSE'),
('Razine Ahmed', 'Bensari', '1049 Galt', 'bensaria97@gmail.com', '514-514-5144', 'TRUE'),
('Charles', 'Charlie', '1234 biol', 'charles@charlie.com', '438-438-4388', 'FALSE');

