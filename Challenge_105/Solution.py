def main():
	T = int(input())
	for _ in range(T):
		a, b = [int(i) for i in input().split()]
		
		limit = 10 ** 9 + 7
		# In-built function to calculate a ** b % limit
		print(pow(a, b, limit))
		

main()