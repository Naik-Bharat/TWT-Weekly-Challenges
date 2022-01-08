# This function returns the number (in base) that is equivalent to num (in decimal)
def change_base(base : int, num : int):
	remainder_stack = []    # stack of remainders when repeatedly divided by base

	while num > 0:
		remainder = num % base
		remainder_stack.append(remainder)
		num = num // base

	binary_digits = []    # reverse of remainder_stack i.e. array of string values of value in base
	while remainder_stack:
		binary_digits.append(str(remainder_stack.pop()))

	return ''.join(binary_digits)

# This function will return the smallest base that will have the num (in decimal) filled with 1's (in output base)
def One(num : int):
	# The smallest base that will have just 1's will have the maximum number of 1's
	
	# 'base' is the base that we are converting the decimal number into
	for base in range(2, num):
		num_in_base = change_base(base, num)    # num_in_base is the value of the number in 'base'
		bool_output = True    # boolean if the number is filled with 1's
		# checking if the 'num_in_base' is filled with 1's
		for char in str(num_in_base):
			if char != "1":
				bool_output = False

		# if num_in_base is filled with 1's
		if bool_output == True:
			break
	
	return base

def main():
	N = int(input())
	for _ in range(N):
		num = int(input())
		print(One(num))


main()