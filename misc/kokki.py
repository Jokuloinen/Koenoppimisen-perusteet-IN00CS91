class chef():
	def __init__(self, name):
		self.name = name

	def doSalad(self):
		print("made salad")

	def doSoup(self):
		print("made soup")

	def introduce(self):
		print(self.name)

class italianChef(chef):
	def doPasta(self):
		print("made pasta")


kokki = chef("joku juu")
kokki.introduce()
kokki.doSalad()
kokki.doSoup()


kokki2 = italianChef("Giorno Giovanna")
kokki2.introduce()
kokki2.doPasta()