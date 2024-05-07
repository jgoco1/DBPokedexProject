insert into PD.regions(region_id, region_name) values (NEXTVAL(PD.reg_seq), 'Kanto');

insert into PD.types(type_id, type_name, weakness_id, resistance_id) values (NEXTVAL(PD.type_seq), 'Grass', NULL, NULL);

insert into PD.abilities(ability_ID, ability_name, ability_type_id, ability_cost, ability_dmg) values (NEXTVAL(pd.abil_seq), "Leech Seed", 1, 2, 20);

insert into PD.settlements(settlement_ID, region_ID, settlement_name) values (NEXTVAL(pd.sett_seq), 1, "Pallet Town");

insert into PD.pokemon(pokemon_num, type_id, pokemon_name, region_id, evolution_id, base_hp, retreat_cost, ability_one_ID, ability_two_ID) 
	values (NEXTVAL(PD.poke_seq), 1, "Bulbasaur", 1, 2, 70, 2, 1, NULL); 
