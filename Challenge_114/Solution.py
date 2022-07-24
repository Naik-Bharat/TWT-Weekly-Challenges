def main():
	T = int(input())    # Number of test cases
	for _ in range(T):
		N = int(input())    # Number of elements in array
		array1 = [int(i) for i in input().split()]
		array2 = [int(i) for i in input().split()]

		# dictionary that would store the count the difference of indices of every number in the arrays
		diff_dict = {}

		for index in range(N):
			# if element in array1 is not in array2
			try:
				difference = index - array2.index(array1[index])
				if difference < 0:
					difference += N
				# if difference not already in diff_dict
				try:
					diff_dict[difference] += 1
				except KeyError:
					diff_dict[difference] = 1
			
			except ValueError:
				pass

		if diff_dict.values():
			print(max(diff_dict.values()))
		else:
			print(0)

main()