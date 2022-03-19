# This function will check if for the given length, all subsequences of the length are unique.
# It will return True if all subsequences are unique
def unique_sequence(sequence : str, length : int):
	# start_index is the starting index of the subsequnce we are checking now
	for start_index in range(0, len(sequence) - length + 1):
		# 'subsequnce' is the subsequnce of the sequence of given length that we are checking now
		subsequence = sequence[start_index:start_index + length]
		
		# second_start_index is the starting index of the second_subsequnce we are comparing with subsequence
		for second_start_index in range(start_index + 1, len(sequence) - length + 1):
			# 'second_subsequence' is the subsequence we are comparing 'subsequence' with
			second_subsequence = sequence[second_start_index:second_start_index + length]
			if subsequence == second_subsequence:
				return False
	return True

def main():
	T = int(input())    # Number of test cases
	for _ in range(T):
		N = int(input())    # Length of sequence
		sequence = input()    # Sequence of colors of houses
		for length in range(1, N + 1):
			if unique_sequence(sequence, length):
				print(length)
				break

main()