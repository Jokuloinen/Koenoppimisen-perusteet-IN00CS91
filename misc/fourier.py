import math
import numpy as np
import matplotlib.pyplot as plt


def myFourierFunc(data):#expects a numpy.ndarrayn
	signalData = data.tolist()
	fourierData = [ ]
	for i in range(0, len(signalData)):
		localFourrierCos = 0
		localFourrierSin = 0
		for ii in range(0, len(signalData)):
			localFourrierCos = localFourrierCos + signalData[ii] * math.cos( 2 * np.pi * i * ii / len(signalData) )
			localFourrierSin = localFourrierSin + signalData[ii] * math.sin( 2 * np.pi * i * ii / len(signalData) )
		
		#en tiiä vaikutta hyvältä idealta... varmaan turhaa laskea sekä sin että cos, mutta kerta on laskettu valitaan ilman mitään syytä isompi
		if localFourrierCos > localFourrierSin:
			fourierData.append(localFourrierCos)
		else:
			fourierData.append(localFourrierSin)

	return np.asarray(fourierData)




hzAlue = np.arange( 0, 1, 1/1000 )
#signals
signal1 = np.cos( 2 * np.pi *   10 * hzAlue )
signal2 = np.cos( 2 * np.pi *  100 * hzAlue )
#signal3 = np.cos( 2 * np.pi *  500 * hzAlue )

#signal to fourier
mixSignal = signal1+signal2
#mixSignal = signal1+signal2+signal3


plt.figure(1)
#plot raw signal
plt.subplot(3,1,1)
plt.plot( mixSignal )
#plot using numpy fourier function
plt.subplot(3,1,2)
plt.plot( np.abs( np.fft.fft( mixSignal ) / ( hzAlue.size ) ) )
#plot my fourier function results
plt.subplot(3,1,3)
plt.plot( np.abs( myFourierFunc( mixSignal ) / ( hzAlue.size ) ) )

plt.show()