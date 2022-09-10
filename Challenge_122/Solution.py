# number of test cases
t = int(input())
for _ in range(t):
	N = int(input())
	chat = str(input())
	chat = chat.split()
	for index, word in enumerate(chat):
		if index == 0:
			print(word, end = "")
		else:
			if word == word.upper():
				print(word.lower(), end = "")
			else:
				print(word, end = "")
		if index == N - 1:
			print()
		else:
			print("", end = " ")