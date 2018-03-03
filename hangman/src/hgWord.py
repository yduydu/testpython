class hgWord():
	def __init__(self, word):
		assert word.isalpha()
		self.word = word.lower()
		self.nbLettersLeft = len(word) 
		self.foundLetters = set()
		self.nbTry = 0
		
	def guessLetter(self, letterIn):
		self.nbTry+=1
		letter = letterIn.lower()
		if letter in self.word and letter not in self.foundLetters:
			self.foundLetters.add(letter)
			self.nbLettersLeft -= self.word.count(letter)
		else:
			return "letter not in the word"
		if self.nbLettersLeft == 0:
			return f"word found in {self.nbTry} try"
		else:
			return "letter in the word"
			
	def displayWord(self):
		displayWord = ""
		for letter in self.word:
			if letter in self.foundLetters:
				displayWord = displayWord + letter + " "
			else:
				displayWord = displayWord + "_ "
		return displayWord