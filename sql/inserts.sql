-- noinspection SqlNoDataSourceInspectionForFile

INSERT INTO items (loanable,itemType)
VALUES
('Y','BOOK'),
('Y','BOOK'),
('Y','BOOK'),
('Y','BOOK'),
('Y','BOOK'),
('Y','BOOK'),
('Y','BOOK'),
('Y','BOOK'),
('Y','BOOK'),
('Y','BOOK'),
('Y','BOOK'),
('Y','BOOK'),
('Y','BOOK'),
('Y','BOOK'),
('Y','BOOK'),
('N','MAGAZINE'),
('N','MAGAZINE'),
('N','MAGAZINE'),
('N','MAGAZINE'),
('N','MAGAZINE'),
('N','MAGAZINE'),
('N','MAGAZINE'),
('N','MAGAZINE'),
('N','MAGAZINE'),
('N','MAGAZINE'),
('N','MAGAZINE'),
('N','MAGAZINE'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MUSIC'),
('Y','MOVIE'),
('Y','MOVIE'),
('Y','MOVIE'),
('Y','MOVIE'),
('Y','MOVIE'),
('Y','MOVIE'),
('Y','MOVIE'),
('Y','MOVIE'),
('Y','MOVIE'),
('Y','MOVIE'),
('Y','MOVIE'),
('Y','MOVIE');

-- noinspection SqlNoDataSourceInspection
INSERT INTO prints (itemId,title,author,num_pages,publisher,year_published,language,isbn_10,isbn_13) -- Books
VALUES 
(1,'Fifty Shades of Grey','E. L. James',514,'Vintage Books',2011,'English','0345803485','978-0345803481'),
(2,'The Subtle Art of Not Giving a F*ck','Mark Manson',224,'Harper',2016,'English','0062641549','978-0062641540'),
(3,'Of Mice and Men','John Steinbeck',112,'Penguin Books',1993,'English','0140177396','978-0140177398'),
(4,'The Intelligent Investor','Benjamin Graham',640,'Harper Business; REV edition',2006,'English','0060555665','978-0060555665'),
(5,'Rich Dad Poor Dad','Robert T. Kiyosaki',336,'Plata Publishing; Second edition',2017,'English','1612680194','978-1612680194'),
(6,'The Elements of Pizza','Ken Forkish',256,'Ten Speed Press',2016,'English','160774838X','978-1607748380'),
(7,'The Five Element','Razine Bens',459,'Za Publish',2018,'English','0345803123','978-0062641512'),
(8,'The Big MAC','Mark BigMac', 233, 'FoodAndBooks',2017,'German, English','0140337396','978-0011641540'),
(9,'The Big Three','Jeremy Steinfield',599,'MarketPub',2016,'Arabic, English','0345803499','978-0166677398'),
(10,'Grapes of Wrath','John Steinbeck',241,'Penguin Publishing',1931,'English','7593648531','834-7593648531'),
(11,'Le monde sans Faim','George Lecavalier',53,'Access Litterature',1994,'French','9301756562','123-9301756562'),
(12,'People are Animals','Jane Joyce', 347,'Worldwide',2008,'English','9044591234','892-9044591234'),
(13,'The Giver','Lois Lowry',240,'HMH Books for Young Readers',2014,'English', '0544336267','978-0544336261'),
(14,'Leonis','Mario Francis',300,'Les Intouchables ',2004,'French', '2895491380','978-2895491385'),
(15,'Cravings: Hungry for More','Chrissy Teigen',256,'Clarkson Potter',2018,'English', '1524759724','978-1524759728');


INSERT INTO prints (itemId,title,publisher,year_published,language,isbn_10,isbn_13) -- Magazines
VALUES
(16,'Design News','UBM','1946','English','9000119407','987-9000119407'),
(17,'Bon Appétit','Craig Kostelic','1956','French','9000066990','987-9000066990'),
(18,'House Beautiful','Hearst Magazines','1996','English','9000186422','987-9000186422'),
(19,'Sports Illustrated Magazine','Meredith Corporation',2018,'English',NULL,NULL),
(20,'Food & Wine Magazine','Meredith Corporation',2018,'English',NULL,NULL),
(21,'Truckin Magazine','The Enthusiast Network',2018,'English',NULL,NULL),
(22,'Le Monde','Le Monde Publishing',2005,'French','8937293950','847-8937293950'),
(23,'Cosmopolitan','No Name Publishing',2015,'English','5723957738','920-5723957738'),
(24,'Actuary Weekly','CPA',2004,'English','9504762930','583-9504762930'),
(25,'Gym and Fitness Magazine','BuzzFit',2018,'English',NULL,NULL),
(26,'PC Magazine','Ziff Davis',2018,'English',NULL,NULL),
(27,'Car Magazine','Bauer Consumer Media',2018,'English',NULL,NULL);


INSERT INTO medias (itemId,mediaType,title,release_date,artist,label,asin) -- Musics
VALUES
(28,'CD','Stormy Monday','1990-12-12','The Allman Brothers Band','At Fillmore East','1234567890'),
(29,'CD','The Chipmunk Song','1959-12-12','Ross Bagdasarian Sr.','Liberty','3456789012'),
(30,'CD','Green Christmas','1958-12-02','Stan Freberg','Capitol Records','2345678901') ,
(31,'CD','Bangarang','2011-12-23','Skrillex','Big Beat, Atlantic, OWSLA','B005FLX1HS'),
(32,'Vinyl','Another One Bites The Dust','1980-12-21','Queen','EMI','B00EX6LCNG'),
(33,'CD','Starlight','2006-09-04','Muse','Warner Bros.','B002CNUSFK'),
(34,'CD','Wake me up in September','2001-04-02','Lincooln Park','DC-Label','2345633345'),
(35,'CD','I am ZA Best','2018-03-03','Rassiol Bambini','Xtreme Muzik','2323498901'),
(36,'CD','Hello Good Morning','1976-03-27','Gorgio Lancini','Fedrolia','1905678901'),
(37,'Vinyl','House of Balloons','2011-03-21','The Weeknd','XO','B011IOGYL0'),
(38,'CD','Thursday','2011-08-18','The Weeknd','XO','B010NUQNGQ'),
(39,'Digital','Echoes of Silence','2011-12-22','The Weeknd','Universal Republic Records','B00TINRK9E'),
(40,'Vinyl','The Reign of Kindo EP','2011-02-11','The Reign of Kindo','Independant', NULL),
(41,'Digital','The Mountain','2013-04-21','Haken','Universal',NULL),
(42,'CD','Best Of the Commodores','1990-05-30','Commodores','Motown',NULL);


INSERT INTO medias (itemId,title,director,producer,actors,languages,subtitles,dubbed,release_date,runtime) -- Movie
VALUES
(43,'Spider-Man','Sam Raimi','Laura Ziskin, Ian Bryce','Raz Bens, Suruthi Priya, Naimur Namur','English, French','Spanish, French, English, Arabic','English, French, German, Hindi','2002-04-29',121),
(44,'The super MAC','Raz Booboo','Nicolas Samaha','Nocolas Samaha, Joshua Butler','Arabic, French, English','Arabic, French, English','Arabic, French, English','2017-01-01',129),
(45,'The Big Fish','Rami Eldiaz','Barbara Samaha','Nocolas Saluti, Josh Aller','French, English','French, English','Arabic, French, English, Spanish, Mandarin','2006-05-01',139),
(46,'Ride Along 2','Tim Story','Will Packer, Ice Cube, Matt Alvarez, Larry Brezner','Kevin Hart, Ice Cube, Ken Jeong, Benjamin Bratt, Olivia Munn, Bruce McGill','English','English, French, Arabic, Chinese, Spanish','English, Spanish, French, Hindi, Russian','2016-01-15',102),
(47,'Just Go With It','Dennis Dugan','Adam Sandler, Jack Giarraputo, Heather Parry','Adam Sandler, Jennifer Aniston, Nick Swardson, Brooklyn Decker, Dave Matthews, Bailee Madison, Nicole Kidman','English','English, French','English, French','2011-01-11',117),
(48,'The Fate of the Furious','F. Gary Gray','Neal H. Moritz, Vin Diesel, Michael Fottrell, Chris Morgan','Vin Diesel, Dwayne Johnson, Jason Statham, Michelle Rodriguez, Tyrese Gibson, Chris "Ludacris" Bridges, Scott Eastwood, Nathalie Emmanuel, Elsa Pataky, Kurt Russell, Charlize Theron','English','English, French, Spanish','English, French','2017-04-14',136),
(49,'The Dark Knight','Christopher Nolan','Emma Thomas, Charles Roven, Christopher Nolan','Christian Bale, Michael Caine, Health Ledger','English, French','Spanish, French, English, Arabic','English, French, German, Hindi','2008-07-14',152),
(50,'The Nun','Corin Hardy','Peter Safran, James Wan','Demian Bichir, Taissa Farmiga, Jonas Bloquet','Arabic, French, English','Arabic, French, English','Arabic, French, English','2018-09-07',96),
(51,'Rush Hour','Brett Ratner', 'Roger Birnbaum, Jonathan Glickman, Arthur M. Sarkissian','Jackie Chan, Chris Tucker','French, English','French, English','Arabic, French, English, Spanish, Mandarin','1998-09-18',98),
(52,'Bee Movie','Simon J. Smith','Jerry Seinfeld','Jerry Seinfeld, Renée Zellweger','English','English, French, Spanish','French, Spanish, Italian','2007-11-02',91),
(53,'Deadpool','Tim Miller','Simon Kinberg, Ryan Reynolds','Ryan Reynolds, Morena Baccarin, T.J. Miller','English','English, French, Spanish','French, Spanish, Italian','2016-02-08',108),
(54,'The Shawshank Redemption','Frank Darabont','Niki Marvin','Tim Robbins, Morgan Freeman, Bob Gunton','English','English, French, Spanish','French, Spanish, Italian','1994-09-10',142);

/*
INSERT INTO users (firstName,lastName,address,email,pswd,phone,privilegeLevel)
VALUES
('Justin','Malone','950 real street, Montreal','justind.malone@domain.ca','tester','514-514-5145','ADMIN'),
('Alex', 'Baker','42 Baker street, Sherbrooke','alex.baker1997@domain.ca','tester','514-514-5165','CLIENT'),
('Alfred','Augustus','5716 Summer boulevard, Quebec City','AA@domain.ca','tester','418-385-3893','CLIENT'),
('Razine Ahmed','Bensari','1049 Galt','bensaria97@gmail.com','tester','514-514-5144','ADMIN'),
('Charles','Charlie','1234 biol','charles@charlie.com','tester','438-438-4388','CLIENT'),
('Vincent','Cerri','2356 rue de vigeois','vincent.cerri@gmail.com','tester','514-591-1642','ADMIN'),
('Emilio','Phish','P Sherman 42 Wallaby Way','emilio.phish@yahoo.ca','tester','456-975-7726','CLIENT'),
('Julia','Runia','5081 Rue Taillon','julia.runia@live.ca','tester','450-999-9879','CLIENT'),
('SURUTHI','R','Number 8, Test, QC, CA.','suruthi@gmail.com','tester','9629923077','ADMIN'),
('EXAMPLE','NOADMIN','Number 15, Test, QC, CA.','EXAMPLE@gmail.com','tester','123456789','CLIENT'),
('ADMIN','D','Number 88, Test, QC, CA.','ADMIN@gmail.com','tester','5678941234','CLIENT'),
('Naimur','Rashid','12243 Chemin Du Roi','naimur.rashid@gmail.com','tester','514-937-1337','ADMIN'),
('Abel','Tesfaye','65 Spencer Avenue','abel.tesfaye@xo.ca','tester','647-824-4331','CLIENT'),
('Aubrey','Graham','82 Queen Street','drizzy@ovo.ca','tester','647-233-0489','CLIENT'),
('Nicolas','Samaha','272 Rue Montpellier','nicolasnsamaha@hotmail.com','tester','514-623-4325','ADMIN'),
('Hugh','Jethighs','555 Nroad','hughjethighs@gmail.com','tester','754-837-8475','CLIENT'),
('Po','Zhu','54 Young Street','Po.Zhu@gmail.com','tester','444-474-4747','CLIENT');
*/
