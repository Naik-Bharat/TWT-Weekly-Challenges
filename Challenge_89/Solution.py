# This function returns if the matrix is filled with 1's given the first and last indexes of row and column
def is_filled_with_1s(matrix : list, row_start : int, row_end : int, col_start : int, col_end : int):
	output = True    # boolean whether it is filled with 1's or not
	for row in range(row_start, row_end):
		for col in range(col_start, col_end):
			if matrix[row][col] != 1:
				output = False
	return output

# This function returns the area of the largest rectangle that is filled with just 1s
def largest_area(matrix : list, no_rows : int, no_cols : int):
	max_area = 0    # Maximum area of the rectangle
	for row_start in range(no_rows):
		for row_end in range(row_start + 1, no_rows + 1):
			for col_start in range(no_cols):
				for col_end in range(col_start + 1, no_cols + 1):
					if is_filled_with_1s(matrix, row_start, row_end, col_start, col_end):
						area = (row_end - row_start) * (col_end - col_start)    # Area of the rectangle that is currently being parsed
						if max_area < area:
							max_area = area
						
	return max_area

def main():
	N = int(input())    # Number of test cases
	change_int = lambda x : [int(i) for i in x]    # This function will return a list with int values in x
	for _ in range(N):
		no_cols, no_rows = change_int(input().split())
		matrix = []    # The matrix we are working with
		for row in range(no_rows):
			matrix.append(change_int(input().split()))
		print(largest_area(matrix, no_rows, no_cols))


main()