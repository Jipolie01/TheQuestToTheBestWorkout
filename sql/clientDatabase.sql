BEGIN TRANSACTION;
CREATE TABLE "subscription" (
	`subscriptionName`	TEXT,
	`price`	INT,
	PRIMARY KEY(subscriptionName),
	FOREIGN KEY(`subscriptionName`) REFERENCES clienInfo ( subscriptionName )
);
INSERT INTO `subscription` VALUES ('easy','17,99');
INSERT INTO `subscription` VALUES ('smart','19,99');
INSERT INTO `subscription` VALUES ('flex','23,99');
CREATE TABLE "logInfo" (
	`rfidNumber`	TEXT,
	`username`	TEXT,
	`password`	TEXT,
	`email`	TEXT,
	PRIMARY KEY(rfidNumber),
	FOREIGN KEY(`rfidNumber`) REFERENCES clientInfo ( rfidNumber )
);
INSERT INTO `logInfo` VALUES ('[12,235,179,213,129]','user2','user2','user2@hotmail.com');
INSERT INTO `logInfo` VALUES ('[52,188,189,222,235]','user1','user1','user1@hotmail.com');
CREATE TABLE "clientInfo" (
	`rfidNumber`	TEXT,
	`surname`	TEXT,
	`name`	TEXT,
	`gender`	TEXT,
	`cellphoneNumber`	TEXT,
	`adresNumber`	INT,
	`zipcode`	TEXT,
	`subscriptionName`	TEXT,
	PRIMARY KEY(rfidNumber)
);
INSERT INTO `clientInfo` VALUES ('[52,188,189,222,235]','Branderhorst','Rohit','male','06-61927142',130,'7891DM','easy');
INSERT INTO `clientInfo` VALUES ('[12,235,179,213,129]','van Rijs','Katrien','female','06-76193384',90,'1764HT','smart');
CREATE TABLE "adresInfo" (
	`zipcode`	TEXT,
	`adresNumber`	INTEGER,
	`street`	TEXT,
	`town`	TEXT,
	`country`	TEXT,
	PRIMARY KEY(zipcode,adresNumber),
	FOREIGN KEY(`zipcode`) REFERENCES clientInfo ( zipcode ),
	FOREIGN KEY(`adresNumber`) REFERENCES clientInfo ( adresNumber )
);
INSERT INTO `adresInfo` VALUES ('7891DM',130,'Melde','Klazienaveen','Nederland');
INSERT INTO `adresInfo` VALUES ('1764HT',90,'Irissenstraat','Breezand','Nederland');
COMMIT;
