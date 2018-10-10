INSERT INTO books (title,author,num_pages,publisher,year_published,language,isbn_10,isbn_13)
VALUES 
('Fifty Shades of Grey','E. L. James',514,'Vintage Books',2011,'English', '0345803485','978-0345803481'),
('The Subtle Art of Not Giving a F*ck','Mark Manson',224,'Harper',2016,'English','0062641549','978-0062641540'),
('Of Mice and Men','John Steinbeck',112,'Penguin Books',1993,'English','0140177396','978-0140177398'),
('The Intelligent Investor: The Definitive Book on Value Investing','Benjamin Graham','Paperback',640,'Harper Business; REV edition',2006,'English','9780060555665','978-0060555665'),
('Rich Dad Poor Dad: What the Rich Teach Their Kids About Money That the Poor and Middle Class Do Not!','Robert T. Kiyosaki','Paperback',336,'Plata Publishing; Second edition',2017,'English','1612680194','978-1612680194'),
('The Elements of Pizza: Unlocking the Secrets to World-Class Pies at Home','Ken Forkish','Hardcover',256,'Ten Speed Press',2016,'English','160774838X','978-1607748380'),
('The Giver','Lois Lowry',240,'HMH Books for Young Readers',2014,'English', '0544336267','978-0544336261'),
('Leonis','Mario Francis',300,'Les Intouchables ',2004,'French', '2895491380','978-2895491385'),
('Cravings: Hungry for More','Chrissy Teigen',256,'Clarkson Potter',2018,'English', '1524759724','978-1524759728');

INSERT INTO magazines (title,publisher,year_published,language,isbn_10,isbn_13)
VALUES
('Sports Illustrated Magazine','Meredith Corporation',2018,'English',NULL,NULL),
('Food & Wine Magazine','Meredith Corporation',2018,'English',NULL,NULL),
('Truckin Magazine','The Enthusiast Network',2018,'English',NULL,NULL),
('Gym and Fitness Magazine','BuzzFit',2018,'English',NULL,NULL),
('PC Magazine','Ziff Davis',2018,'English',NULL,NULL),
('Car Magazine','Bauer Consumer Media',2018,'English',NULL,NULL);


INSERT INTO musics (type,title,release_date,artist,label,asin)
VALUES
('Vinyl','House of Balloons','2011-03-21','The Weeknd','XO','B011IOGYL0'),
('CD','Thursday','2011-08-18','The Weeknd','XO','B010NUQNGQ'),
('Digital','Echoes of Silence','2011-12-22','The Weeknd','Universal Republic Records','B00TINRK9E');

INSERT INTO clients (firstName,lastName,addresse,email,phone,isAdmin)
VALUES
	('Vincent','Cerri','2356 rue de vigeois','vincent.cerri@gmail.com','514-591-1642',TRUE),
	('Emilio','Phish','P Sherman 42 Wallaby Way','emilio.phish@yahoo.ca','456-975-7726',FALSE),
	('Julia','Runia','5081 Rue Taillon','julia.runia@live.ca','450-999-9879',FALSE),
    ('Naimur','Rashid','12243 Chemin Du Roi','naimur.rashid@gmail.com','514-937-1337',TRUE),
	('Abel','Tesfaye','65 Spencer Avenue','abel.tesfaye@xo.ca','647-824-4331',FALSE),
	('Aubrey','Graham','82 Queen Street','drizzy@ovo.ca','647-233-0489',FALSE),
	('Nicolas','Samaha','272 Montpellier','nicolasnsamaha@hotmail.com','514-623-4325',FALSE);

