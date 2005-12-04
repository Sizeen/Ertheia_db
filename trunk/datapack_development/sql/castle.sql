-- ---------------------------
-- Table structure for castle
-- ---------------------------
CREATE TABLE IF NOT EXISTS castle (
  id INT NOT NULL default 0,
  name varchar(25) NOT NULL,
  taxPercent INT NOT NULL default 15,
  treasury INT NOT NULL default 0,
  siegeDate DECIMAL(20,0) NOT NULL default 0,
  siegeDayOfWeek INT NOT NULL default 7,
  siegeHourOfDay INT NOT NULL default 20,
  PRIMARY KEY  (name),
  KEY id (id)
);

Insert Into castle Values (1, 'Gludio', 0, 0, 0, 7, 20);
Insert Into castle Values (2, 'Dion', 0, 0, 0, 7, 20);
Insert Into castle Values (3, 'Giran', 0, 0, 0, 1, 16);
Insert Into castle Values (4, 'Oren', 0, 0, 0, 1, 16);
Insert Into castle Values (5, 'Aden', 0, 0, 0, 7, 20);
Insert Into castle Values (6, 'Innadril', 0, 0, 0, 1, 16);
