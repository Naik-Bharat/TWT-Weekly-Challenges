def main():
	T = int(input())    # Number of test cases
	for _ in range(T):
		Q = int(input())    # Number of queries
		# array data would store the data of the array in a dictionary format. Format would be {index in array: value at index in array}
		array_data = {}
		for query_no in range(Q):
			query = input().split()
			if query[0] == "P":
				try:
					print(array_data[int(query[1])])
				# if value for index has not already been set up
				except KeyError:
					print(0)

			if query[0] == "S":
				array_data[int(query[1])] = int(query[2])
				
			if query[0] == "A":
				try:
					array_data[int(query[1])] += 1
				# if value for index has not already been set up
				except KeyError:
					array_data[int(query[1])] = 1


main()