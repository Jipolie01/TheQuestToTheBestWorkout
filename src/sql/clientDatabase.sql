CREATE TABLE IF NOT EXISTS costumerInfo (
	costumerID		 INT UNSIGNED		NOT NULL AUTO_INCREMENT,
    surname			 VARCHAR(30)		NOT NULL DEFAULT '',
    name 			 VARCHAR(30)		NOT NULL DEFAULT '',
    gender			 VARCHAR(6)			NOT NULL DEFAULT '',
    RFIDNumber		 CHAR(20)			NOT NULL DEFAULT '[00,000,000,000,000]',
    cellphoneNumber  CHAR(11)			NOT NULL DEFAULT '06-00000000',
    subscriptionName VARCHAR(5)			NOT NULL DEFAULT '',
    
    primary key(costumerID)
);