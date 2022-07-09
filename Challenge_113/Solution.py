def main():
	T = int(input())    # Number of test cases
	for _ in range(T):
		# n is the number of houses, x is the max number of dogs John can tolerate
		n, x = map(int, (input().split()))

		# street_info will store the number of dogs that have been kept at a house
		str_to_int = lambda x : [int(i) for i in x]
		street_info = input().split()
		street_info = str_to_int(street_info)

		# psum is the precedence sum of all the dogs from starting
		psum = [0]
		for house_no in range(n):
			if house_no == 0:
				psum.append(street_info[0])
			else:
				psum.append(psum[house_no] + street_info[house_no])
		
		max_length = 0

		# for every starting position
		for starting_point in range(n + 1):
			# for every ending position possible to increase max_length
			for ending_point in range(starting_point + max_length, n + 1):
				if psum[ending_point] - psum[starting_point] <= x:
					max_length = ending_point - starting_point
				else:
					break
		
		print(max_length)


main()