# This function prints the row column to num in square of given length
def solve(length : int, num : int):
	# If num not in square or if it repeats multiple times in the square
	if (num > length * (length + 1) / 2) or (num == 0 and length > 2):
		print("BAD INPUT")
	# Specific case
	elif num == 0 and length == 2:
		print("2 1")
	elif num == 0 and length == 1:
		print("BAD INPUT")
	else:
		# for every row
		for row in range(1, length + 1):
			# value of col for respective row
			col = length - ((length * (length + 1) / 2) - ((length - row) * (length - row + 1) / 2) - num)
			# if num exists in this row
			if col <= length:
				print(f'{row} {int(col)}')
				break


def main():
	T = int(input())    # number of test cases
	for _ in range(T):
		# s is the length of the square and v is the number we have to find on the paper
		s, v = [int(i) for i in input().split()]
		solve(s, v)


main()