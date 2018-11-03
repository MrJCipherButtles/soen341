-- All users
SELECT * FROM users;

-- All clients
SELECT * FROM users WHERE privilegeLevel = 'CLIENT';

-- All Administrators
SELECT * FROM users WHERE privilegeLevel = 'ADMIN';

-- All Prints
SELECT * FROM prints INNER JOIN items ON itemId = id;

-- All Books
SELECT * FROM prints INNER JOIN items ON itemId = id WHERE itemType = 'BOOK';

-- All Magazines
SELECT * FROM prints INNER JOIN items ON itemId = id WHERE itemType = 'MAGAZINE';

-- All Medias
SELECT * FROM medias INNER JOIN items ON itemId = id;

-- All Movies
SELECT * FROM medias INNER JOIN items ON itemId = id WHERE itemType = 'MOVIE';

-- All Musics
SELECT * FROM medias INNER JOIN items ON itemId = id WHERE itemType = 'MUSIC';

-- All Loans
SELECT * FROM loans;