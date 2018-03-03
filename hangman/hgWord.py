class hgWord():
	def __init__(self, word):
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
			return "not in the word"
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
		
		
# basic unit test		
if __name__ == "__main__":
	testWord = hgWord("test")
	dw = testWord.displayWord()
	print(dw)
	assert dw == "_ _ _ _ "
	
	print("test letter T")
	gl = testWord.guessLetter('t')
	dw = testWord.displayWord()
	print(gl)
	print(dw)

	print("test letter A")
	gl = testWord.guessLetter('a')
	dw = testWord.displayWord()
	print(gl)
	print(dw)
	
	print("test letter S")
	gl = testWord.guessLetter('s')
	dw = testWord.displayWord()	
	print(gl)
	print(dw)
			
	print("test letter E")
	gl = testWord.guessLetter('e')
	dw = testWord.displayWord()	
	print(gl)
	print(dw)