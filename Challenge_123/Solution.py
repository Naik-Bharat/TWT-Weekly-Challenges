t = int(input())    # number of test cases
for _ in range(t):
	case = int(input())
	while case != 1:
		print(int(case), end=" ")
		if case % 2 == 0:
			case /= 2
		else:
			case = case * 3 + 1
	print(1)