def solve(operands: list[int], operators: list[str]):
	while "*" in operators:
		for index, operator in enumerate(operators):
			if operator == "*":
				operands[index] *= operands[index + 1]
				del operands[index + 1]
				del operators[index]
				break

	while len(operands) != 1:
		if operators[0] == "+":
			operands[0] += operands[1]
			del operands[1]
			del operators[0]
		elif operators[0] == "-":
			operands[0] -= operands[1]
			del operands[1]
			del operators[0]

	result = operands[0]

	if result < 0:
		return -1 * (-1 * result % (10 ** 9 + 7))
	else:
		return result % (10 ** 9 + 7)


def main():
	T = int(input())    # Number of test cases
	for _ in range(T):
		expression = input().split()
		# If there is just an operand given in the expression
		if len(expression) == 1:
			print(expression[0])
			continue
		operators = []
		operands = []
		for index, num in enumerate(expression):
			if index % 2 == 0:
				operands.append(int(num))
			else:
				operators.append(num)

		print(solve(operands, operators))


main()
