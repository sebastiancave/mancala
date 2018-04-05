#######################################
######       Mancala.py          ######
#######################################

#This is the *Working* version (see email)
#a little buggy, can easily be cleaned up over intensives.
#sometimes i have closed my computer and when i opened it, despite not changing anything, ran into problems that were not there before.
#if you are having trouble with the game, change the starting arrays to test the features.
#thanks <3

class Board:

	def __init__(self):

		#sets the board to its starting state
		self.p1_bank = [0]
		self.p2_bank = [0]
		self.p1_row =[4, 4, 4, 4, 4, 4]
		self.p2_row = [4, 4, 4, 4, 4, 4]
		self.whosTurn = 0

	def Display(self):

		#displays CURRENT board state
		print("   ", end="")

		for items in self.p1_row:

			print ("|", items ,end="")

		print("|")

		print (self.p1_bank ,end="")

		for x in range (0,6):

			print ("- - ", end="")

		print (self.p2_bank)

		print("   ", end="")

		for items in self.p2_row:

			print ("|" ,items ,end="")

		print("|")

	def makeMove(self, spot):

		if self.whosTurn == 0:

			#initialize temp_list
			temp_list = []
			temp_list += self.p1_row[::-1]
			temp_list += self.p1_bank
			temp_list += self.p2_row

			#create pips variable and make a copy of sopt
			pips = temp_list[spot]

			temp_spot = spot

			#takes all pips out of the spot
			temp_list[spot] = 0

			#while there are pips remaining in your hand
			while pips > 0:

				#go to the next spot
				temp_spot += 1

				#if you are at the end of the board, go back to the beginning
				if temp_spot == len(temp_list):

					temp_spot = 0

				#save the last spot you drop at
				if pips == 1:
					lastDrop = temp_spot

				#drop a pip there
				temp_list[temp_spot] += 1
				pips -= 1

			#set board arrays to their new values from temp_list
			final_row = temp_list[:6]
			self.p1_row = final_row[::-1]
			self.p1_bank[0] = temp_list[6]
			self.p2_row = temp_list[7:]

			#make it the other player's turn

		if self.whosTurn == 1:

			#initialize temp_list
			temp_list = []
			temp_list += self.p2_row
			temp_list += self.p2_bank
			temp_list += self.p1_row[::-1]

			#create pips variable and make a copy of sopt
			pips = self.p2_row[spot]
			temp_spot = spot

			#takes all pips out of the spot
			temp_list[spot] = 0

			#while there are pips remaining in your hand
			while pips > 0:

				#go to the next spot
				temp_spot += 1

				#if you are at the end of the board, go back to the beginning
				if temp_spot == len(temp_list):

					temp_spot = 0

				#save the last spot you drop at
				if pips == 1:
					lastDrop = temp_spot

				#drop a pip there
				temp_list[temp_spot] += 1
				pips -= 1				#set board arrays to their new values from temp_list self.p2_row = temp_list[:6]
				self.p2_bank[0] = temp_list[6]
				final_row = temp_list[7:]
				self.p1_row = final_row[::-1 ]
				self.p2_row = temp_list[:6]

		#if your last drop was in an empty space, steal all pieces in both the space you landed in and the space opposite yours (only if the empty space you landed on was on your side of the board)
		stolenPips = 0
		if temp_list[lastDrop] == 1 and lastDrop != 6:
			if lastDrop < 6:
				stolenPips += self.p1_row[lastDrop]
				self.p1_row[lastDrop] = 0
				stolenPips += self.p2_row[lastDrop]
				self.p2_row[lastDrop] = 0
				print ('Nice Steal!')

		#make it the other player's turn but only if your last drop wasnt in the bank
		if lastDrop != 6:
			if self.whosTurn == 0:
				self.whosTurn = 1
				self.p1_bank[0] += stolenPips
			elif self.whosTurn == 1:
				self.whosTurn = 0
				self.p2_bank[0] += stolenPips

		if lastDrop == 6:
			print('Take another turn')

	def isGameOver(self):

		#takes in a board state and returns true if the board state is an ending state

		if self.sum(self.p1_row) == 0:

			return True

		elif self.sum(self.p2_row) == 0:

			return True

		else:

			return False

	def sum(self, array):

		#gives the sum of any array in the board object

		total = 0

		for item in array:

			total += item

		return total

class HumanPlayer:

	def __init__(self, number):

		self.number = number

	def getNextMove(self, Board):

		#returns the spot where the move takes place

		while True:

			moveSpot = int(input("What spot would you like to move?"))

			if Board.whosTurn == 0:

				if moveSpot < 6:

					if Board.p1_row[moveSpot] != 0:

						return moveSpot

			if Board.whosTurn == 1:

				if moveSpot < 6:

					if Board.p2_row[moveSpot] != 0:

						return moveSpot

def rules():
	print('The board spaces are numbered 012345 for each side COUNTERCLOCKWISE')
	print('Have fun!')
	print('Kevin Spacey')

def play():	

	rules()

	#creates two player objects

	board = Board()
	player = HumanPlayer(1)

	while board.isGameOver() == False:
		board.Display()
		board.makeMove(player.getNextMove(board))

	if board.p1_bank > board.p2_bank:

		print ('GAME OVER, Player 1 Wins')

	elif board.p2_bank > board.p1_bank:

		print ('GAME OVER, Player 2 Wins')

	else:

		print ('Wow, a Tie')

play()
