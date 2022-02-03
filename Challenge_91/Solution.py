def most_water_in_sandbox(no_lines : int, sandbox : list):
	most_water = 0
	for start_index in range(0, no_lines - 1):
		for end_index in range(start_index + 1, no_lines):
			area = min(sandbox[start_index], sandbox[end_index]) * (end_index - start_index)
			if area > most_water:
				most_water = area

	return most_water


# This function returns the list of elements converted into integers 
change_int = lambda x : [int(i) for i in x]

def main():
	T = int(input())
	for _ in range(T):
		num_lines = int(input())
		sandbox = change_int(input().split())
		print(most_water_in_sandbox(num_lines, sandbox))

main()