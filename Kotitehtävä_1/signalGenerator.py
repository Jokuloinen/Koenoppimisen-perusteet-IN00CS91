import tehtävänanto.tehtava1 as t

def virheArvo(arv, min, max, default):
	#if type is wrong
	if arv.isdigit() == False:
		return default
	if int(arv) < 0:
		return default


	#if number is incorrect
	if int(arv) > int(max):
		return default
	if int(arv) < int(min):
		return default
	return arv


aika = input("Anna aika 1-10 sekunttia: ")
aika = virheArvo(aika, 1, 10, 1)
print("aika =", aika)


taajuus = input("Anna taajuus 0-500: ")
taajuus = virheArvo(taajuus, 0, 500, 2)
print("taajuus =", taajuus)


plm = input("Anna tulostettavien pisteiden lukumäärä < aika*Fs = aika*1000: ")
plm = virheArvo(plm, 0, aika*1000, aika*1000)
print("tulostus lukumäärä =", plm)



obj = t.signalAnalyser(1000,int(aika))	# luodaan objekti, jonka konstruktorille Fs = 100 Hz ja t = 2s
obj.create(int(taajuus))		# käytetään objektin create funktiota, missä f = 2 Hz
obj.plot(0,int(plm))			# käytetään objektin plot funktiota, plotataan väli 0 - 50 näytettä.