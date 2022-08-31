import math

def printSetMiddle(setsudan):
	iter = 0
	for i in setsudan:
		if iter == int(math.floor(len(setsudan)/2)):#toimii joskus johtuu varmaan siitä että mun koodi on väärin tai setti allokaattori on outo 
			print(i)
		iter += 1

def printDictMiddle(dicti):
	iter=0
	for i in dct:
		if iter == int(math.floor(len(dicti)/2)):
			print(i + ":" + str(dicti[i]))
		iter += 1




lst = [ 'c', "lst",   64  ]
tpl = (  32,   't', "tpl" )
st  = { "st", "76",   "s" }
dct = { "avain":5, "pari":42, "lista":78}



print(lst[1])
print(tpl[1])
printSetMiddle(st)
printDictMiddle(dct)