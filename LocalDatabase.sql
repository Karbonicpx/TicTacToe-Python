CREATE DATABASE IF NOT EXISTS ranking;

use ranking;

CREATE TABLE IF NOT EXISTS players(
	id int not null primary key auto_increment,
    playername varchar(30),
	wins int not null,
    totalmatches int not null
);
