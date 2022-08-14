T = int(input())    # Number of test cases
for _ in range(T):
	# Number of seconds
	s = int(input())
	print(f'{s // 3600} {(s % 3600) // 60} {s % 60}')