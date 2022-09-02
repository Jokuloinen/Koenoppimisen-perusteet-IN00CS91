import math

def printCommonMiddle(mv):#multivalue
	iter = 0
	for i in mv:
		if iter == int(math.floor(len(mv)/2)):
			if type(mv) is dict: 
				print(i + ":" + str(mv[i]))
			else:
				print(i)
			break
		iter += 1


lst = [       'c',     "lst",	     64  ] #list
tpl = (        32,	 't',	   "tpl" ) #tuple
st  = {	     "st",	"76",	     "s" } #set
dct = { "avain":5, "pari":42, "lista":78 } #dictionary


printCommonMiddle(lst)
printCommonMiddle(tpl)
printCommonMiddle(st)
printCommonMiddle(dct)
print("")