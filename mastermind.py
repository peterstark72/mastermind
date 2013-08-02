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



def feedback(code, pegs):
	'''Returns a tuple with the number of correct guesses (black) and the number of correct colors but wrong positions (white)

	Args:
	code - the code, e.g. (1,2,3,4)
	pegs - the guess, e.g. (1,1,1,1)

	Example: 
	The code (1,2,3,4) and guess (1,1,1,1), will return (1,0) since only the first peg is correct. 

	'''

	#First, get a set of all positions, e.g. 0,1,2,3,..
	positions = set(range(len(code)))	


	#Set of all black positions
	black_positions = set(
		[pos for pos, peg in enumerate(pegs) if peg==code[pos]])
	blacks = len(black_positions)


	#Remaining set is all less the blacks
	remains_pos = positions - black_positions
	remains = [code[pos] for pos in remains_pos]

	whites = 0
	awarded_duplicates = set()
	for pos in remains_pos:
		color = pegs[pos]
		if color in remains and pegs.count(color) <= code.count(color):
			whites += 1
		elif color in remains and color not in awarded_duplicates:
			whites += 1
			awarded_duplicates.add(color)

	
	return blacks, whites



def calcperm(blacks, whites, colors = DEFAULT_COLORS, holes = DEFAULT_HOLES):
	'''Calculates remaining possibilities'''

	p = 1

	#In white pos we know one color is wrong
	for n in range(whites):
		p *= colors-1

	#In remaining pos still any color could be right		
	for n in range(holes - blacks - whites):
		p *= colors

	return p



class Game:
	'''A simple Matstermind game. 

	'''

	MAX_TURNS = 10

	def __init__(self, colors=DEFAULT_COLORS, holes=DEFAULT_HOLES):
		'''Creates a game with give colors and number of holes'''
		self.code = gencode(colors, holes)
		self.number_of_holes = len(self.code)
		self.colors = colors
		self.holes = holes
		self.turns = 0
		self.blacks = 0
		self.whites = 0

		print "New game. Colors: {} in {} holes".format(range(colors), holes)

		print "".join(map(str,self.code))


	def guess(self, pegs):
		'''Returns True of the guess is correct or the number of turns equals Game.MAX_TURNS'''
		self.turns += 1
		self.blacks, self.whites = feedback(self.code, pegs)
		
		if self.turns == Game.MAX_TURNS or self.number_of_holes == self.blacks:
			return True


	@property			
	def possibilities(self):
		return calcperm(self.blacks, self.whites, self.colors, self.holes)



if __name__ == '__main__':

	g = Game()

	done = False
	while not done:

		s = raw_input()
		if s == 'q' or not s:
			sys.exit("Goodbye!")

		pegs = map(int, list(s))
		done = g.guess(pegs)

		print "{:>20}, {} ({})".format(g.blacks, g.whites, g.possibilities)

	
	sys.exit("You made it!")













	