def main():
	T = int(input())    # Number if test cases
	for _ in range(T):
		N = int(input())    #Number of diamonds
		# array of size of diamonds
		diamondSizeArray = input().split()
		diamondSizeArray = [int(i) for i in diamondSizeArray]
		# diamondInfo stores the number of diamonds of a paticular size of diamond
		diamondInfo = {}
		for diamond in diamondSizeArray:
			if diamond in diamondInfo.keys():
				diamondInfo[diamond] += 1
				continue
			diamondInfo[diamond] = 1

		maxDiamondSize = 0
		maxDiamonds = max(diamondInfo.values())
		for diamondSize, numDiamonds in diamondInfo.items():
			if numDiamonds == maxDiamonds:
				if diamondSize > maxDiamondSize:
					maxDiamondSize = diamondSize

		print(f'{maxDiamonds} {maxDiamondSize}')

main()