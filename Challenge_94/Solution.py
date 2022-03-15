import itertools

def is_prime(num : int):
	if num == 1:
		return False
	elif num < 4:
		return True
	elif num % 2 == 0:
		return False
	elif num % 3 == 0:
		return False
	i = 5
	while i ** 2 < num:
		if num % i == 0 or num % (i + 2) == 0:
			return False
		i += 6
	return True

def main():
	T = int(input())    # Number of test cases
	for _ in range(T):
		a = sorted(itertools.permutations(input()), reverse = True)
		for _ in a:
			num = int("".join(list(_)))
			if is_prime(num):
				print(num)
				break

main()
