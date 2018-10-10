INSERT INTO books (title,author,num_pages,publisher,year_published,language,isbn_10,isbn_13)
VALUES
('Fifty Shades of Grey','E. L. James',514,'Vintage Books',2011,'English', '0345803485','978-0345803481'),
('The Subtle Art of Not Giving a F*ck','Mark Manson',224,'Harper',2016,'English','0062641549','978-0062641540'),
('Of Mice and Men','John Steinbeck',112,'Penguin Books',1993,'English','0140177396','978-0140177398'),
('The Intelligent Investor: The Definitive Book on Value Investing','Benjamin Graham','Paperback',640,'Harper Business; REV edition',2006,'English','9780060555665','978-0060555665'),
('Rich Dad Poor Dad: What the Rich Teach Their Kids About Money That the Poor and Middle Class Do Not!','Robert T. Kiyosaki','Paperback',336,'Plata Publishing; Second edition',2017,'English','1612680194','978-1612680194'),
('The Elements of Pizza: Unlocking the Secrets to World-Class Pies at Home','Ken Forkish','Hardcover',256,'Ten Speed Press',2016,'English','160774838X','978-1607748380'),
('Eyewitness Travel Guides: 2019.','Bostrom, Annie',140,'Book list edition',2019,'English','9781111112','978-9781111112'),
('Educated: A Memoir','Tara Westover',493,'Random House Large Print',2018,'English','1635461855','978-1635461855'),
('The Mars Room','Simon and Schuster',256,'Test Example Press',2018,'English','1982100753','978-1982100753');


INSERT INTO musics (type, title, release_date, artist, label, asin)
VALUES
('CD','Stormy Monday','1990-12-12','The Allman Brothers Band','At Fillmore East','1234567890'),
('CD','The Chipmunk Song','1959-12-12','Ross Bagdasarian Sr.','Liberty','3456789012'),
('CD','Green Christmas','1958-12-02','Stan Freberg','Capitol Records','2345678901') ,
('CD','Bangarang','2011-12-23','Skrillex','Big Beat, Atlantic, OWSLA','B005FLX1HS'),
('Vinyl','Another One Bites The Dust','1980-12-21','Queen','EMI','B00EX6LCNG'),
('CD','Starlight','2006-09-04','Muse','Warner Bros.','B002CNUSFK'),
('CD', 'Wake me up in September', '2001-04-02', 'Lincooln Park', 'DC-Label', '2345633345'),
('CD', 'I am ZA Best', '2018-03-03', 'Rassiol Bambini', 'Xtreme Muzik', '2323498901'),
('CD', 'Hello Good Morning', '1976-03-27', 'Gorgio Lancini', 'Fedrolia', '1905678901');

INSERT INTO magazines (title, publisher, year_published, language, isbn_10, isbn_13)
VALUES 
('Design News','UBM','1946','English','9000119407','987-9000119407'),
('Bon Appétit','Craig Kostelic','1956','French','9000066990','987-9000066990'),
('House Beautiful','Hearst Magazines','1996','English','9000186422','987-9000186422') ;

INSERT INTO clients(firstName, lastName, addresse, email, phone, isAdmin)
values
('SURUTHI','R','Number 8, Test, QC, CA.','suruthi@gmail.com','9629923077','TRUE'),
('EXAMPLE','NOADMIN','Number 15, Test, QC, CA.','EXAMPLE@gmail.com','123456789','FALSE'),
('ADMIN','D','Number 88, Test, QC, CA.','ADMIN@gmail.com','5678941234','TRUE');