from Entity.DatabaseConnection import DatabaseConnection

class pokedex:
	def __init__(self, dbconn):
		self.dbconn = dbconn
	
	def add_type(self, type_name):
		"""
		Adds a new type to the database.
		
		Parameters:
		type_name (str): The name of the type to add.
		
		Returns:
		None
		"""
		cursor = self.dbconn.getConnection().cursor()
		cursor.execute("INSERT INTO types (type_name) VALUES (%s)", (type_name,))
		self.dbconn.getConnection().commit()
		cursor.close()
		
	def getTypes(self):
		"""
		Gets all types from the database.
		
		Parameters:
		None
		
		Returns:
		types (list): A list of all types.
		"""
		cursor = self.dbconn.getConnection().cursor()
		cursor.execute("SELECT * FROM types")
		types = cursor.fetchall()
		cursor.close()
		return types
		
	def add_ability(self, ability_name, cost, damage):
		"""
		Adds a new ability to the database.
		
		Parameters:
		ability_name (str): The name of the ability to add.
		cost (int): The cost of the ability.
		damage (int): The damage of the ability.
		
		Returns:
		None
		"""
		cursor = self.dbconn.getConnection().cursor()
		cursor.execute("INSERT INTO abilities (ability_name, cost, damage) VALUES (%s, %s, %s)", (ability_name, cost, damage))
		self.dbconn.getConnection().commit()
		cursor.close()
		
	def getAbilities(self):
		"""
		Gets all abilities from the database.
		
		Parameters:
		None
		
		Returns:
		abilities (list): A list of all abilities.
		"""
		cursor = self.dbconn.getConnection().cursor()
		cursor.execute("SELECT * FROM abilities")
		abilities = cursor.fetchall()
		cursor.close()
		return abilities
		
	def add_region(self, region_name):
		"""
		Adds a new region to the database.
		
		Parameters:
		region_name (str): The name of the region to add.
		
		Returns:
		None
		"""
		cursor = self.dbconn.getConnection().cursor()
		cursor.execute("INSERT INTO regions (region_name) VALUES (%s)", (region_name,))
		self.dbconn.getConnection().commit()
		cursor.close()
		
	def getRegions(self):
		"""
		Gets all regions from the database.
		
		Parameters:
		None
		
		Returns:
		regions (list): A list of all regions.
		"""
		cursor = self.dbconn.getConnection().cursor()
		cursor.execute("SELECT * FROM regions")
		regions = cursor.fetchall()
		cursor.close()
		return regions
