import pdb 


def add_on(num):
	result = num + 1
	print(result)
	return result


def main():
	pdb.set_trace()
	for num in range(0, 10):
		add_on(num)


if __name__ == "__main__":
	main()