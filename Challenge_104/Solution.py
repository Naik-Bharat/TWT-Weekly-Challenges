# This function returns list of integer values of all elements in x
str_to_int = lambda x: [int(i) for i in x]

# This function returns the maximum desire value possible in consecutively
def max_desire_value(N : int, array : list):
	# Maximum value of any subarray
	max_value = 0
	
	# List of all possible starting index value for subarray
	starting_index_list = []

	# List of all possible ending index value for subarray
	ending_index_list = []

	for index in range(N):
		if array[index] < 0:
			if index + 1 < N:
				starting_index_list.append(index + 1)
			if index - 1 >= 0:
				ending_index_list.append(index - 1)

	if 0 not in starting_index_list:
		starting_index_list.append(0)
		starting_index_list.sort()

	if N - 1 not in ending_index_list:
		ending_index_list.append(N - 1)

	# parsing through all subarrays
	for starting_index in starting_index_list:
		for ending_index in ending_index_list:
			if ending_index >= starting_index:
				value = sum(array[starting_index: ending_index + 1])
				# print(f'{starting_index} {ending_index} {value}')
				if value > max_value:
					max_value = value
				# In this case max value of desire value would not be possible with this 'starting_index'
				elif value <= 0:
					break

	return max_value


def main():
	T = int(input())    # Number of test cases
	for _ in range(T):
		N = int(input())    # Number of demons
		# list of desire value of all demons
		array = str_to_int(str(input()).split())
		print(max_desire_value(N, array))


main()
