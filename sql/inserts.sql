INSERT INTO books (title,author,num_pages,publisher,year_published,language,isbn_10,isbn_13)
VALUES 
('Fifty Shades of Grey','E. L. James',514,'Vintage Books',2011,'English','0345803485','978-0345803481'),
('The Subtle Art of Not Giving a F*ck','Mark Manson',224,'Harper',2016,'English','0062641549','978-0062641540'),
('Of Mice and Men','John Steinbeck',112,'Penguin Books',1993,'English','0140177396','978-0140177398'),
('The Intelligent Investor: The Definitive Book on Value Investing','Benjamin Graham',640,'Harper Business; REV edition',2006,'English','0060555665','978-0060555665'),
('Rich Dad Poor Dad: What the Rich Teach Their Kids About Money That the Poor and Middle Class Do Not!','Robert T. Kiyosaki',336,'Plata Publishing; Second edition',2017,'English','1612680194','978-1612680194'),
('The Elements of Pizza: Unlocking the Secrets to World-Class Pies at Home','Ken Forkish',256,'Ten Speed Press',2016,'English','160774838X','978-1607748380'),
('The Five Element','Razine Bens',459,'Za Publish',2018,'English','0345803123','978-0062641512'),
('The Big MAC','Mark BigMac', 233, 'FoodAndBooks',2017,'German, English','0140337396','978-0011641540'),
('The Big Three','Jeremy Steinfield',599,'MarketPub',2016,'Arabic, English','0345803499','978-0166677398'),
('Grapes of Wrath','John Steinbeck',241,'Penguin Publishing',1931,'English','7593648531','834-7593648531'),
('Le monde sans Faim','George Lecavalier',53,'Access Litterature',1994,'French','9301756562','123-9301756562'),
('People are Animals','Jane Joyce', 347,'Worldwide',2008,'English','9044591234','892-9044591234'),
('The Giver','Lois Lowry',240,'HMH Books for Young Readers',2014,'English', '0544336267','978-0544336261'),
('Leonis','Mario Francis',300,'Les Intouchables ',2004,'French', '2895491380','978-2895491385'),
('Cravings: Hungry for More','Chrissy Teigen',256,'Clarkson Potter',2018,'English', '1524759724','978-1524759728');


INSERT INTO magazines (title,publisher,year_published,language,isbn_10,isbn_13)
VALUES
('Design News','UBM','1946','English','9000119407','987-9000119407'),
('Bon Appétit','Craig Kostelic','1956','French','9000066990','987-9000066990'),
('House Beautiful','Hearst Magazines','1996','English','9000186422','987-9000186422'),
('Sports Illustrated Magazine','Meredith Corporation',2018,'English',NULL,NULL),
('Food & Wine Magazine','Meredith Corporation',2018,'English',NULL,NULL),
('Truckin Magazine','The Enthusiast Network',2018,'English',NULL,NULL),
('Le Monde','Le Monde Publishing',2005,'French','8937293950','847-8937293950'),
('Cosmopolitan','No Name Publishing',2015,'English','5723957738','920-5723957738'),
('Actuary Weekly','CPA',2004,'English','9504762930','583-9504762930'),
('Gym and Fitness Magazine','BuzzFit',2018,'English',NULL,NULL),
('PC Magazine','Ziff Davis',2018,'English',NULL,NULL),
('Car Magazine','Bauer Consumer Media',2018,'English',NULL,NULL);


INSERT INTO musics (type,title,release_date,artist,label,asin)
VALUES
('CD','Stormy Monday','1990-12-12','The Allman Brothers Band','At Fillmore East','1234567890'),
('CD','The Chipmunk Song','1959-12-12','Ross Bagdasarian Sr.','Liberty','3456789012'),
('CD','Green Christmas','1958-12-02','Stan Freberg','Capitol Records','2345678901') ,
('CD','Bangarang','2011-12-23','Skrillex','Big Beat, Atlantic, OWSLA','B005FLX1HS'),
('Vinyl','Another One Bites The Dust','1980-12-21','Queen','EMI','B00EX6LCNG'),
('CD','Starlight','2006-09-04','Muse','Warner Bros.','B002CNUSFK'),
('CD','Wake me up in September','2001-04-02','Lincooln Park','DC-Label','2345633345'),
('CD','I am ZA Best','2018-03-03','Rassiol Bambini','Xtreme Muzik','2323498901'),
('CD','Hello Good Morning','1976-03-27','Gorgio Lancini','Fedrolia','1905678901'),
('Vinyl','House of Balloons','2011-03-21','The Weeknd','XO','B011IOGYL0'),
('CD','Thursday','2011-08-18','The Weeknd','XO','B010NUQNGQ'),
('Digital','Echoes of Silence','2011-12-22','The Weeknd','Universal Republic Records','B00TINRK9E'),
('Vinyl','The Reign of Kindo EP','2011-02-11','The Reign of Kindo','Independant', NULL),
('Digital','The Mountain','2013-04-21','Haken','Universal',NULL),
('CD','Best Of the Commodores','1990-05-30','Commodores','Motown',NULL);


INSERT INTO movies (title,director,producer,actors,languages,subtitles,dubbed,release_date,runtime)
VALUES
<<<<<<< HEAD
	('Vincent','Cerri','2356 rue de vigeois','vincent.cerri@gmail.com','514-591-1642',TRUE),
	('Emilio','Phish','P Sherman 42 Wallaby Way','emilio.phish@yahoo.ca','456-975-7726',FALSE),
	('Julia','Runia','5081 Rue Taillon','julia.runia@live.ca','450-999-9879',FALSE),
    ('Naimur','Rashid','12243 Chemin Du Roi','naimur.rashid@gmail.com','514-937-1337',TRUE),
	('Abel','Tesfaye','65 Spencer Avenue','abel.tesfaye@xo.ca','647-824-4331',FALSE),
	('Aubrey','Graham','82 Queen Street','drizzy@ovo.ca','647-233-0489',FALSE),
	('Nicolas','Samaha','272 Montpellier','nicolasnsamaha@hotmail.com','514-623-4325',FALSE);
=======
('Spider-Man','Sam Raimi','Laura Ziskin, Ian Bryce','Raz Bens, Suruthi Priya, Naimur Namur','English, French','Spanish, French, English, Arabic','English, French, German, Hindi','2002-04-29','121'),
('The super MAC','Raz Booboo','Nicolas Samaha','Nocolas Samaha, Joshua Butler','Arabic, French, English','Arabic, French, English','Arabic, French, English','2017-01-01','129'),
('The Big Fish','Rami Eldiaz','Barbara Samaha','Nocolas Saluti, Josh Aller','French, English','French, English','Arabic, French, English, Spanish, Mandarin','2006-05-01','139'),
('Ride Along 2','Tim Story','Will Packer, Ice Cube, Matt Alvarez, Larry Brezner','Kevin Hart, Ice Cube, Ken Jeong, Benjamin Bratt, Olivia Munn, Bruce McGill','English','English, French, Arabic, Chinese, Spanish','English, Spanish, French, Hindi, Russian','2016-01-15','102'),
('Just Go With It','Dennis Dugan','Adam Sandler, Jack Giarraputo, Heather Parry','Adam Sandler, Jennifer Aniston, Nick Swardson, Brooklyn Decker, Dave Matthews, Bailee Madison, Nicole Kidman','English','English, French','English, French','2011-01-11','117'),
('The Fate of the Furious','F. Gary Gray','Neal H. Moritz, Vin Diesel, Michael Fottrell, Chris Morgan','Vin Diesel, Dwayne Johnson, Jason Statham, Michelle Rodriguez, Tyrese Gibson, Chris "Ludacris" Bridges, Scott Eastwood, Nathalie Emmanuel, Elsa Pataky, Kurt Russell, Charlize Theron','English','English, French, Spanish','English, French','2017-04-14','136'),
('The Dark Knight','Christopher Nolan','Emma Thomas, Charles Roven, Christopher Nolan','Christian Bale, Michael Caine, Health Ledger','English, French','Spanish, French, English, Arabic','English, French, German, Hindi','2008-07-14','152'),
('The Nun','Corin Hardy','Peter Safran, James Wan','Demian Bichir, Taissa Farmiga, Jonas Bloquet','Arabic, French, English','Arabic, French, English','Arabic, French, English','2018-09-07','96'),
('Rush Hour','Brett Ratner', 'Roger Birnbaum, Jonathan Glickman, Arthur M. Sarkissian','Jackie Chan, Chris Tucker','French, English','French, English','Arabic, French, English, Spanish, Mandarin','1998-09-18','98');

>>>>>>> e8353788d279947bd5299ce11a8238b7a5b9ed83

INSERT INTO clients (firstName,lastName,address,email,phone,isAdmin)
VALUES
('Justin','Malone','950 real street, Montreal','justind.malone@domain.ca','514-514-5145','FALSE'),
('Alex', 'Baker','42 Baker street, Sherbrooke','alex.baker1997@domain.ca','514-514-5165','FALSE'),
('Alfred','Augustus','5716 Summer boulevard, Quebec City','AA@domain.ca','418-385-3893','FALSE'),
('Razine Ahmed','Bensari','1049 Galt','bensaria97@gmail.com','514-514-5144','TRUE'),
('Charles','Charlie','1234 biol','charles@charlie.com','438-438-4388','FALSE'),
('Vincent','Cerri','2356 rue de vigeois','vincent.cerri@gmail.com','514-591-1642','TRUE'),
('Emilio','Phish','P Sherman 42 Wallaby Way','emilio.phish@yahoo.ca','456-975-7726','FALSE'),
('Julia','Runia','5081 Rue Taillon','julia.runia@live.ca','450-999-9879','FALSE'),
('SURUTHI','R','Number 8, Test, QC, CA.','suruthi@gmail.com','9629923077','TRUE'),
('EXAMPLE','NOADMIN','Number 15, Test, QC, CA.','EXAMPLE@gmail.com','123456789','FALSE'),
('ADMIN','D','Number 88, Test, QC, CA.','ADMIN@gmail.com','5678941234','TRUE'),
('Naimur','Rashid','12243 Chemin Du Roi','naimur.rashid@gmail.com','514-937-1337','TRUE'),
('Abel','Tesfaye','65 Spencer Avenue','abel.tesfaye@xo.ca','647-824-4331','FALSE'),
('Aubrey','Graham','82 Queen Street','drizzy@ovo.ca','647-233-0489','FALSE');