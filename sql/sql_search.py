import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()

	promt = """
	Select the operation that you want to perform [1-5]:
	1. Average
	2. MAx
	3. Min
	4. Sum
	5. Exit
	"""

	# loop until user enters a valid operation number[1-5]
	while True:
		# get user input
		x = input(promt)

		# if user enters any choice from 1-4
		if x in set(["1", "2", "3", "4"]):
			# parse the corresponding operation text
			operation = {1:"avg", 2:"max", 3:"min", 4:"sum"}[int(x)]

			# retrieve data
			c.execute("SELECT {}(num) from numbers".format(operation))

			# fetchone() retrieves one record from the query
			get = c.fetchone()

			# output result to screen
			print(operation + ": %f" % get[0])

		# f user enters 5
		elif x == "5":
			print("EXit")

			# exit loop 
			break
