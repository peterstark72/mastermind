#!/usr/bin/env python
'''mastermind.py

Functions to generate code, give feedback and calculate remaining number of possibilities.


Rules are based on: 
http://en.wikipedia.org/wiki/Mastermind_(board_game)


'''

import random
import math
import sys
import operator


'''As default we use class Mastermind from 1972. 

'''
DEFAULT_COLORS = 6
DEFAULT_HOLES = 4



def gencode(colors=DEFAULT_COLORS, holes=DEFAULT_HOLES):
	'''Returns a random code pattern. 

	Args: 
	colors - the number of colores (6 in classic MM)
	holes - the number of holes (4 in classic MM)

	'''
	return [random.randrange(colors) for c in range(holes)]



def feedback(code, guesses):
	'''Returns a tuple with the number of correct guesses (black) and the number of correct colors but wrong positions (white)

	Args:
	code - the code, e.g. (1,2,3,4)
	guesses - the guess, e.g. (1,1,1,1)

	Example: 
	The code (1,2,3,4) and guess (1,1,1,1), will return (1,0) since only the first peg is correct. 

	'''

	#First, get a set of all positions, e.g. 0,1,2,3,..
	positions = set(range(len(code)))	

	#Set of all black positions
	blacks = set(
		[pos for pos, guess in enumerate(guesses) if guess==code[pos]])

	#Remaining set is all less the blacks
	remains = positions - blacks
	remain_code = set([code[pos] for pos in remains])
	remain_guess = set([guesses[pos] for pos in remains])
	
	whites = remain_code & remain_guess
	

	return len(blacks), len(whites)



class Game:

	def __init__(self):
		self.code = gencode()
		self.turns = 0


	def makeguess(self, pegs):
		self.feedback = feedback(self.code, pegs)
		self.turns += 1



if __name__ == '__main__':

	g = Game()

	done = False
	while not done:

		s = raw_input()
		if s == 'q':
			sys.exit("Goodbye!")

		guess = map(int, s.split())
		g.makeguess(guess)

		print "{:>20}".format(g.feedback)

		if g.feedback == (4,0):
			sys.exit("You made it!")












	