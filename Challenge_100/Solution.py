from math import ceil


def main():
	T = int(input())    # Number of test cases
	for _ in range(T):
		N = int(input())
		print(ceil(N/100))

main()