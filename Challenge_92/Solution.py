def main():
	T = int(input())    # Number of test cases
	for _ in range(T):
		R = int(input())    # Number of rows
		
		# R(R+1)/2 bytes for *'s, R bytes for '\n' and modulo by 4096
		print(int((R ** 2 + 3 * R) / 2) % 4096)

main()