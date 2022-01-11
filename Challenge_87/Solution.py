# This function returns True if the number (in base) equivalent to 'num' (in decimal) is filled with 1's, it returns False if number (in base) is not filled with 1's
def change_base(base : int, num : int):
	while num > 0:
		remainder = num % base
		# if number (in base) has anything other than 1
		if remainder != 1:
			return False
		num = num // base

	return True

# This function will return the smallest base that will have the number (in base) equivalent to 'num' (in decimal) filled with just 1's
# The smallest base that will be filled with just 1's will have the maximum number of 1's
def One(num : int):
	# 'base' is the base that we are converting the decimal number into
	for base in range(2, num):
		# If 'base' is even, then 111... (in 'base') has to be odd, so it will not be equal to 'num'
		if num % 2 == 0 and base % 2 == 0:
			continue
		correct_result = change_base(base, num)    # correct_result tells if this base is giving required result
		if correct_result != False:
			break
	
	return base

def main():
	N = int(input())    # Number of test cases
	for _ in range(N):
		num = int(input())
		print(One(num))


main()