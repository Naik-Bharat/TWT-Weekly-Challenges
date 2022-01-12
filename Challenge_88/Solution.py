# This function returns the sum of digits of a number until sum is in one digit
def sum_digits(num : int):
	sum = 0    # sum of digits
	while num != 0:
		sum += num % 10    # add digit at ones placefrom 'num'
		num //= 10    # quotient when 'num' divided by 10

	# If sum not in one digit
	if sum >= 10:
		return sum_digits(sum)    # find sum of digits of 'sum'
	return sum

def main():
	N = int(input())    # Number of test cases
	for _ in range(N):
		num = int(input())
		print(sum_digits(num))

main()
