# This function returns the binary number equivalent to 'num' in decimal
def decimal_to_binary(num : int):
	output = ""
	while num != 0:
		remainder = num % 2
		output += str(remainder)
		num //= 2
	
	return int(output[::-1])


def main():
	T = int(input())    # Number of test cases
	for _ in range(T):
		num1, num2 = input().split()
		print(decimal_to_binary(int(num1, 2) + int(num2, 2)))    # int(num, base) returns the number in decimal equivalent to 'num1' in base

main()