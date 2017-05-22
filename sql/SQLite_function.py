# SQLite Functions

import sqlite3

with sqlite3.connect("new.db") as connection:

	c = connection.cursor()
    
    # create a dictonary of sql queries
	sql = {'average': "SELECT avg(population) FROM population",
		   'maximum': "SELECT max(population) FROM population",
		   'minimum': "SELECT min(population) FROM population",
		   'sum': "SELECT sum(population) FROM population",
		   'count': "SELECT count(city) FROM population"}
	# run each sql query item in the dictionary
	for keys, values in sql.items():
		
		# run sql
		c.execute(values)
		
		# fetchone() retrieves one reord from the query 
		results = c.fethchone()
		
		# output the result to sreen
		print(keys + ":", results[0])
