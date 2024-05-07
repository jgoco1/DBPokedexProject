Create user 'PDUser' IDENTIFIED BY 'osboxes.org';

create database PD;

grant all privileges on PD.* TO 'PDUser';

create table PD.pokemon
(pokemon_num int primary key,
type_id int,
	foreign key(type_id) references PD.types(type_id),
pokemon_name varchar(50),
region_id int,
	foreign key(region_id) references PD.regions(region_id),
evolution_id int,
	foreign key(evolution_id) references PD.pokemon(evolution_id),
base_hp int,
retreat_cost int,
ability_one_ID int,
	foreign key (ability_one_ID) references PD.abilities(ability_ID),
ability_two_ID int,
	foreign key (ability_two_ID) references PD.abilities(ability_ID)
);

create table PD.types
(type_id int primary key,
type_name varchar(50),
weakness_id int,
resistance_id int);

create table PD.abilities
(ability_ID int primary key,
ability_name varchar(100),
ability_type_id int
	foreign key (ability_type_id) references PD.types(type_id),
ability_cost int,
ability_dmg int);

create table PD.regions
(region_ID int primary key,
region_name varchar(50));

create table PD.settlements(
settlement_ID int primary key,
region_ID int,
	foreign key (region_ID) references PD.regions(region_ID),
settlement_name varchar(50)
);

create sequence PD.poke_seq;
create sequence PD.type_seq;
create sequence PD.abil_seq;
create sequence PD.reg_seq;
create sequence PD.sett_seq;
