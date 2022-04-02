# This function converts all elements of a list to integers
str_to_int = lambda x: [int(_) for _ in x]

def main():
	T = int(input())    # Number of test cases
	for _ in range(T):
		# number of test cases, percentage of accuracy required to pass
		num_test_cases, accuracy_percentage = str_to_int(str(input()).split())
		test_cases_result = str(input())
		if test_cases_result.count("Y") / num_test_cases * 100 >= accuracy_percentage:
			print("PASS")
		else:
			print("FAIL")

main()