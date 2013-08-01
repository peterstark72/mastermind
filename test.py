#!/usr/bin/env python

import unittest

import mastermind


class TestMasterMind(unittest.TestCase):

	def test_code(self):
		code = mastermind.gencode()
		self.assertTrue(code)

	def test_duplicates(self):
		'''Duplicate guesses are not counted'''
		code = (1,1,2,2) 
		guess = (1,1,1,2) 

		fb = mastermind.feedback(code, guess)
		self.assertTrue(fb == (3,0))


	def test_duplicates2(self):
		'''Middle 2's do not give white key pegs'''
		code = (1,1,1,2)
		guess = (1,2,2,2)

		fb = mastermind.feedback(code, guess)
		self.assertTrue(fb == (2,0))

	def test_duplicates3(self):
		'''More duplcates in code than guesses'''
		code = [5, 0, 5, 5]
		guess = [5, 5, 3, 2]

		fb = mastermind.feedback(code, guess)
		self.assertTrue(fb == (1,1))
				

	def test_duplicates4(self):
		code = [1, 3, 2, 3]
		guess = [0, 3, 1, 1]

		fb = mastermind.feedback(code, guess)
		self.assertTrue(fb == (1,1))



	def test_correct(self):
		code = (1,2,3,4) 
		guess = (1,2,3,4)

		fb = mastermind.feedback(code, guess)
		self.assertTrue(fb == (4,0))


	def test_wrong(self):
		code = (2,2,2,2)
		guess = (1,1,1,1)

		fb = mastermind.feedback(code, guess)
		self.assertTrue(fb == (0,0))


	def test_misc(self):
		code = (1,2,3,4)
		guess = (4,3,2,1)

		fb = mastermind.feedback(code, guess)
		self.assertTrue(fb == (0,4))


if __name__ == '__main__':
	unittest.main()