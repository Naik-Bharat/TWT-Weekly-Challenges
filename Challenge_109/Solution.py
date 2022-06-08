class Date():
	def __init__(self, date = None):
		if date != None:
			self.month = int(date[:2])
			self.day = int(date[3:])
		else:
			self.month = None
			self.day = None

	# Enters the date as difference of the two dates
	def diff(self, date1, date2):
		if date2.day >= date1.day:
			self.month = date2.month - date1.month
			self.day = date2.day - date1.day
		else:
			self.month = date2.month - date1.month - 1
			# List of number of days for every month
			days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
			self.day = days[date2.month - 2] - date1.day + date2.day

	def __repr__(self):
		return f'{self.month} {self.day}'

def solve(date1, date2):
	date3 = Date()
	date3.diff(date1, date2)
	print(date3)

def main():
	T =  int(input())
	for _ in range(T):
		date1, date2 = map(Date, input().split())
		solve(date1, date2)

main()