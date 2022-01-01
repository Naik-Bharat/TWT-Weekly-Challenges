def solution():
    class Game:
    	def __init__(self, first_chance : str, num_chances : int, order : list):
    		self.board = [".", ".", ".", ".", ".", ".", ".", ".", "."]
    		self.player = first_chance
    		self.num_chances = num_chances
    		self.order = order
    		self.winner = None
    		self.play()
    
    
    	def play(self):
    		for chance in range(self.num_chances):
    			self.board[self.order[chance] - 1] = self.player
    			self.change_player()
    
    		self.check_win()
    
    	
    	def change_player(self):
    		if self.player == "X":
    			self.player = "O"
    		elif self.player == "O":
    			self.player = "X"
    
    
    	def check_win(self):
    		self.check_win_row()
    		self.check_win_column()
    		self.check_win_diagonal()
    
    	def check_win_row(self):
    		if self.board[0] == self.board[1] == self.board[2] != ".":
    			self.winner = self.board[0]
    		elif self.board[3] == self.board[4] == self.board[5] != ".":
    			self.winner = self.board[3]
    		elif self.board[6] == self.board[7] == self.board[8] != ".":
    			self.winner = self.board[6]
    	
    	def check_win_column(self):
    		if self.board[0] == self.board[3] == self.board[6] != ".":
    			self.winner = self.board[0]
    		elif self.board[1] == self.board[4] == self.board[7] != ".":
    			self.winner = self.board[1]
    		elif self.board[2] == self.board[5] == self.board[8] != ".":
    			self.winner = self.board[2]
    
    	def check_win_diagonal(self):
    		if self.board[0] == self.board[4] == self.board[8] != ".":
    			self.winner = self.board[0]
    		elif self.board[2] == self.board[4] == self.board[6] != ".":
    			self.winner = self.board[2]
    
    def main():
    	n = int(input())    # number of test cases
    	for _ in range(n):
    		init_details = str(input())    # Tells which player is playing first 'X' or 'O' and the number of chances in the game
    		init_details = init_details.split()
    		first_chance = init_details[0]
    		num_chances = int(init_details[1])
    		order = str(input())
    		order = [int(i) for i in order.split()]
    		game = Game(first_chance, num_chances, order)
    		if game.winner != None:
    			print(game.winner)
    		else:
    			print("Tie")
    
    
    if __name__=="__main__":
    	main()