# for unit tests, get the source directory in the path
import sys
sys.path.insert(0, '..')

import unittest
from src.hgWord import hgWord

class Test_hgWord(unittest.TestCase):
	'''
	Test the hgWord class
	'''
	#--- test the hgWord function
	def test_hgWordInit(self):
	
		# test 1: incorrect input
		with self.assertRaises(AssertionError):
			testWord = hgWord("as12")
		
		# test 2: normal input
		testWord = hgWord("test")
		self.assertTrue(testWord.word, 'test')
		self.assertTrue(testWord.nbLettersLeft, 4)
		self.assertTrue(testWord.nbTry == 0)
		self.assertFalse(testWord.foundLetters)
		
		# test 3: mixed case input
		testWord = hgWord("TeSt")
		self.assertTrue(testWord.word, 'test')
	
	#--- test the guess letter function
	def test_guessLetter(self):
		testWord = hgWord("test")
		
		str = testWord.guessLetter("s")
		self.assertTrue(testWord.nbLettersLeft, 3)
		self.assertTrue(testWord.foundLetters, {'s'})
		self.assertTrue(testWord.nbTry, 1)
		self.assertTrue(str, "letter in the word")
		
		str = testWord.guessLetter("t")
		self.assertTrue(testWord.nbLettersLeft, 1)
		self.assertTrue(testWord.foundLetters, {'s', 't'})
		self.assertTrue(testWord.nbTry, 2)
		self.assertTrue(str, "letter in the word")
		
		str = testWord.guessLetter("a")
		self.assertTrue(testWord.nbLettersLeft == 1)
		self.assertTrue(testWord.foundLetters, {'s', 't'})
		self.assertTrue(testWord.nbTry, 3)
		self.assertTrue(str, "letter not in the word")
		
		str = testWord.guessLetter("e")
		self.assertTrue(testWord.nbLettersLeft == 0)
		self.assertTrue(testWord.foundLetters, {'s', 't', 'e'})
		self.assertTrue(testWord.nbTry, 4)
		self.assertTrue(str, "word found in 4 try")	
	
	#--- test the display word function
	def test_displayWord(self):
		testWord = hgWord("test")
		display = testWord.displayWord()
		self.assertTrue(display, '_ _ _ _ ')
		
		str = testWord.guessLetter("t")
		display = testWord.displayWord()
		self.assertTrue(display, 't _ _ t ')
		
		str = testWord.guessLetter("e")
		str = testWord.guessLetter("s")
		display = testWord.displayWord()
		self.assertTrue(display, 't e s t ')
		
		
		
		
		

if __name__ == '__main__':
    unittest.main()