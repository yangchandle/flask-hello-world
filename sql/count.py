# SQLite Functions

"""Using the COUNT() function, calculate the total number of orders for each make and model."""

import sqlite3

with sqlite3.connect("car.db") as connection:
	c = connection.cursor()

	# create a dictonary of sql queries
	sql = {'Focus count' : "SELECT count(make) FROM orders WHERE model = 'Focus'",
			'Civic count' : "SELECT count(make) FROM orders WHERE model = 'Civic'",
			'Ranger count' : "SELECT count(make) FROM orders WHERE model = 'Ranger'",
			'Accord count' : "SELECT count(make) FROM orders WHERE model = 'Accord'",
			'Avengar count' : "SELECT count(make) FROM orders WHERE model ='Avenger'",
			}

	# run each sql query item in the dictionary
	for keys, values in sql.items():

		# run sql
		c.execute(values)

		# fetchone() retrieves one record from the query
		result = c.fetchone()

		# output the result to screeen
		print(keys + ":", result[0])
