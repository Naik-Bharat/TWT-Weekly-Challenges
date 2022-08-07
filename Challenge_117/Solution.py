T = int(input())    # Number of test cases
for _ in range(T):
	password = str(input())
	character = str(input())
	print(password.count(character))