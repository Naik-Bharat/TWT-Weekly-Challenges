# Object for matrices
class Matrix:
	def __init__(self, a11, a12, a21, a22):
		self.matrix = [[a11, a12], [a21, a22]]

	# Function for multiplication of matrices
	def __mul__(self, other):
		a11 = (self.matrix[0][0] * other.matrix[0][0] + self.matrix[0][1] * other.matrix[1][0]) % (10 ** 9 + 7)
		a12 = (self.matrix[0][0] * other.matrix[0][1] + self.matrix[0][1] * other.matrix[1][1]) % (10 ** 9 + 7)
		a21 = (self.matrix[1][0] * other.matrix[0][0] + self.matrix[1][1] * other.matrix[1][0]) % (10 ** 9 + 7)
		a22 = (self.matrix[1][0] * other.matrix[0][1] + self.matrix[1][1] * other.matrix[1][1]) % (10 ** 9 + 7)
		return Matrix(a11, a12, a21, a22)

	def __repr__(self):
		return f'{self.matrix[0][0]} {self.matrix[0][1]}\n{self.matrix[1][0]} {self.matrix[1][1]}'


def main():
	T = int(input())
	factorial_dict = {1 : Matrix(1, 1, 1, 0)}
	for _ in range(T):
		num = int(input())
		if num == 0:
			print(0)
			continue
		a = Matrix(1, 1, 1, 0)
		result = Matrix(1, 1, 1, 0)
		pow = 1
		while pow * 2 <= num:
			if pow * 2 not in factorial_dict.keys():
				result = result * result
				factorial_dict[pow * 2] = result
			else:
				result = factorial_dict[pow * 2]
			pow *= 2
		for i in list(factorial_dict.keys())[::-1]:
			if pow == num:
				break
			if pow + i <= num:
				result = result * factorial_dict[i]
				# factorial_dict[pow + 1] = result
				pow += i
		print(result.matrix[0][1])

main()
