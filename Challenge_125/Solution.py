t = int(input())
str_to_int = lambda x: [int(i) for i in x]
for _ in range(t):
	n, sum = str_to_int(input().split())
	arr = str_to_int(input().split())
	count = 0
	start = 0
	end = 0
	current_sum = arr[0]
	while end < n:
		if current_sum == sum:
			count += 1
		if current_sum < sum:
			end += 1
			if end == n:
				break
			current_sum += arr[end]
		else:
			current_sum -= arr[start]
			start += 1
	print(count)