create table if not exists customerInfo (
	customerID		 int unsigned		not null auto_increment,
    surname			 varchar(30)		not null default '',
    name 			 varchar(30)		not null default '',
    gender			 varchar(6)			not null default '',
    RFIDNumber		 char(20)			not null default '[00,000,000,000,000]',
    cellphoneNumber  char(11)			not null default '06-00000000',
    subscriptionName varchar(5)			not null default '',
    
    primary key(customerID)
);

delete from customerInfo where customerID=1;

insert into customerInfo (customerID, surname, name, gender, RFIDNumber, cellphoneNumber, subscriptionName)
	values (1, 'Plugge', 'Riemer', 'male', '[52,188,189,222,235]', '06-80971817', 'flex'); 
insert into customerInfo (customerID, surname, name, gender, RFIDNumber, cellphoneNumber, subscriptionName)
	values (2, 'Breen', 'Trienke', 'female', '[12,235,179,213,129]', '06-82150427', 'smart');

create table if not exists adresInfo (
	customerID		int unsigned	not null auto_increment,
    street			varchar(30)		not null default '',
    zipcode			char(6)			not null default '0000AA',
    adresNumber		varchar(5)		not null default '',
    town			varchar(50)		not null default '',
    country			varchar(20)		not null default 'Nederland',
	
    primary key(customerID),
    foreign key(customerID) references customerInfo(customerID)
);

insert into adresInfo (customerID, street, zipcode, adresNumber, town, country)
	values (1, 'De Beers', '5373CZ', '17', 'Herpen', 'Nederland');
insert into adresInfo (customerID, street, zipcode, adresNumber, town, country)
	values (2, 'Essenseweg', '4709BL', '105', 'Nispen', 'Nederland');

create table if not exists loginInfo (
	customerID		int unsigned	not null auto_increment,
    username		varchar(12)		not null default '',
    password		varchar(40)		not null default '',
    email			varchar(254)	not null default '',
    logedIn			boolean			not null default false,
    
	primary key(customerID),
    foreign key(customerID) references customerInfo(customerID)
);

create table if not exists products (
	subscriptionName varchar(5)			not null default '',
    price			 decimal(4,2)		not null default 00.00,
    
    primary key(subscriptionName)
    #foreign key(subscriptionName) references customerInfo(subscriptionName)
);

insert into products (subscriptionName, price)
	values ('easy', 17.99);
insert into products (subscriptionName, price)
	values ('smart', 19.99);
insert into products (subscriptionName, price)
	values ('flex', 23.99);

create table if not exists customerPerformanceInfo(
	sessionID		int unsigned	not null auto_increment,
	customerID		int unsigned	not null,
    startSession	datetime		not null default '0000-00-00 00:00:00',
    endSession		datetime		not null default '0000-00-00 00:00:00',
    fitnessDevice	varchar(13)		not null default '',
    BurntCalories	smallint(5) 	not null default 0,
    
    primary key(sessionID),
    foreign key(customerID) references customerInfo(customerID)
); 