# This function would return the final output to the expression given the operands and the operator
def solve(operands : list[int], operator : str):
	result = operands[0]

	for index in range(1, len(operands)):
		if operator == "+":
			result += operands[index]
		if operator == "-":
			result -= operands[index]
		elif operator == "*":
			result *= operands[index]

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
		operator = expression[1]
		operands = []
		for index, num in enumerate(expression):
			if index % 2 == 0:
				operands.append(int(num))
	
		print(solve(operands, operator))

main()