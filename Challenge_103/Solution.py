def main():
	T = int(input())    # Number of test cases
	for _ in range(T):
		A = str(input())    # First string
		B = str(input())    # Second string
		count = 0    # Number of instances of B in A
		index = 0    # index by which we are parsing through A
		for character in A:
			if character == B[0]:
				if A[index: index + len(B)] == B:
					count += 1
			index += 1
		
		print(count)


main()