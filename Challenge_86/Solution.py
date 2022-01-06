class Game:
	def __init__(self, first_chance : str, num_chances : int, order : list):
		self.board = [".", ".", ".", ".", ".", ".", ".", ".", "."]
		self.player = first_chance
		self.num_chances = num_chances
		self.order = order
		self.winner = None
		self.play()

	# plays the game
	def play(self):
		for chance in range(self.num_chances):
			self.board[self.order[chance] - 1] = self.player    # sets chance at required chance on the board
			self.change_player()
		self.check_win()
	
	# changes the player from "X" to "O" and vice versa
	def change_player(self):
		if self.player == "X":
			self.player = "O"
		elif self.player == "O":
			self.player = "X"

	# checks for the winner and sets variable "winner" to winner's name
	def check_win(self):
		self.check_win_row()
		self.check_win_column()
		self.check_win_diagonal()

	# checks if there is a winner from any of the rows
	def check_win_row(self):
		if self.board[0] == self.board[1] == self.board[2] != ".":
			self.winner = self.board[0]
			return
		elif self.board[3] == self.board[4] == self.board[5] != ".":
			self.winner = self.board[3]
			return
		elif self.board[6] == self.board[7] == self.board[8] != ".":
			self.winner = self.board[6]
	
	# checks if there is a winner from any of the columns
	def check_win_column(self):
		if self.board[0] == self.board[3] == self.board[6] != ".":
			self.winner = self.board[0]
			return
		elif self.board[1] == self.board[4] == self.board[7] != ".":
			self.winner = self.board[1]
			return
		elif self.board[2] == self.board[5] == self.board[8] != ".":
			self.winner = self.board[2]

	# checks if there is a winner from any of the diagonals
	def check_win_diagonal(self):
		if self.board[0] == self.board[4] == self.board[8] != ".":
			self.winner = self.board[0]
			return
		elif self.board[2] == self.board[4] == self.board[6] != ".":
			self.winner = self.board[2]

def main():
	n = int(input())    # number of test cases
	for _ in range(n):
		init_details = str(input())    # Tells which player is playing first 'X' or 'O' and the number of chances in the game
		init_details = init_details.split()
		first_chance = init_details[0]    # tells who plays the first chance, "X" or "O"
		num_chances = int(init_details[1])    # tells how many chances does it take for the game to end
		order = str(input())
		order = [int(i) for i in order.split()]    # tells the order of chances that is being played
		game = Game(first_chance, num_chances, order)
		if game.winner != None:
			print(game.winner)
		else:
			print("Tie")


main()