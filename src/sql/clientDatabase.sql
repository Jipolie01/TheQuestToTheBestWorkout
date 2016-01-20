create table if not exists costumerInfo (
	costumerID		 int unsigned		not null auto_increment,
    surname			 varchar(30)		not null default '',
    name 			 varchar(30)		not null default '',
    gender			 varchar(6)			not null default '',
    RFIDNumber		 char(20)			not null default '[00,000,000,000,000]',
    cellphoneNumber  char(11)			not null default '06-00000000',
    subscriptionName varchar(5)			not null default '',
    
    primary key(costumerID)
);

insert into costumerInfo (costumerID, surname, name, gender, RFIDNumber, cellphoneNumber, subscriptionName)
values (1, 'Plugge', 'Riemer', 'male', '[52,188,222,235]', '06-80971817', 'flex'); 


create table if not exists adresInfo (
	costumerID		int unsigned	not null auto_increment,
    street			varchar(30)		not null default '',
    zipcode			char(6)			not null default '0000AA',
    adresNumber		varchar(5)		not null default '',
    town			varchar(50)		not null default '',
    country			varchar(20)		not null default 'Nederland',
	
    primary key(costumerID),
    foreign key(costumerID) references costumerInfo(costumerID)
);

insert into adresInfo (costumerID, street, zipcode, adresNumber, town, counrty)
values (1, 'De Beers', '5373CZ', '17', 'Herpen', 'Nederland');

create table if not exists loginInfo (
	costumerID		int unsigned	not null auto_increment,
    username		varchar(12)		not null default '',
    password		varchar(30)		not null default '',
    email			varchar(254)	not null default '',
    
	primary key(costumerID),
    foreign key(costumerID) references costumerInfo(costumerID)
);

insert into loginInfo (costumerID, username, password, email)
values (1, 'Thasce', 'utai6eoquaT', 'RiemerPlugge@teleworm.us');

create table if not exists products (
	subscriptionName VARCHAR(5)			not null default '',
    price			 int(5)				not null default '',
    
    primary key(subscriptionName),
    foreign key(subscriptionName) references costumerInfo(subscriptionName)
);

insert into products (subscriptionName , price)
values ('easy', 17.99);
insert into products (subscriptionName , price)
values ('smart', 19.99);
insert into products (subscriptionName , price)
values ('flex', 23.99);

create table if not exists customerPerformanceInfo(
	customerID		int unsigned	not null auto_increment,
    startSession	datetime		not null default '0000-00-00 00:00:00',
    endSession		datetime		not null default '0000-00-00 00:00:00',
    fitnessDevice	varchar(13)		not null default '',
    BurntCalories	smallint(5) 	not null default 0,
    
    primary key(startSession),
    foreign key(costumerID) references costumerInfo(costumerID)
); 