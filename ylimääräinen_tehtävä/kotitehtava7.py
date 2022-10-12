'''
Tehtävät:
1. Lue kuva4.csv tiedosto pandas kirjaston avulla ja muuta se numpy arrayksi esimerkin mukaisesti

2. Selvitä, minkä kokoinen kuva on ja muokkaa siitä 28x28 pikselin kokoinen kuva, jonka tulostat
   matplotlib kirjaston plt.imshow -komennolla.

3. Selvitä internetistä, kuinka sigmoid funktio voidaan toteuttaa pythonilla ja numpyllä. Tee siitä 
   aliohjelma ja testaa sen toiminta syöttämällä aliohjelmaan sisälle numpy array, jossa 100 kpl
   arvoja -20 ja +20 väliltä. Käytä np.linspace -funktiota tuon datan tekemiseen. Ja lopuksi tulosta
   kuva plt.plot(x,y) -komennolla, missä x = tekemäsi input data ja y = sigmoid funktiosi output.

4. Selvitä (anna opettajan kertoa), miten 784,30,10 -kokoisen neuroverkon output lasketaan. Toteuta tuo laskenta
   numpyn matmul -komentoa ja tekemääsi sigmoid funktiota hyödyntäen. Saat opetetun neuroverkon parametrit w1,w2
   b1, b2 luettua vastaavista csv tiedostoista. Ja lopuksi tulosta neuroverkon kuvasta 4 laskema tulos.

'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import cv2

#def sigmoid(x):                           # tähän voit toteuttaa sigmoid funktiosi.


df = pd.read_csv('kuva4.csv',header=None)  # näin saadaan luettua kaikki rivit
a0 = df.to_numpy()                         # activation a0 tätä voidaan käyttää neuroverkon inputtina
kuva = df.to_numpy();                      # Ja tätä voit sitten muokata kuvan tulostamiseksi

df = pd.read_csv('w1.csv',header=None)     # Tästä tiedostosta luetaan opetetut painokertoimet
w1 = df.to_numpy()                         # w1 = 30x784 matriisi

df = pd.read_csv('w2.csv',header=None)     # Tästä tiedostosta luetaan opetetut painokertoimet
w2 = df.to_numpy()                         # w2 = 10*30 matriisi

df = pd.read_csv('b1.csv',header=None)     # Tästä tiedostosta luetaan opetetut bias arvot
b1 = df.to_numpy()                         # b1 = 30 kpl

df = pd.read_csv('b2.csv',header=None)     # Tästä tiedostosta luetaan opetetut bias arvot
b2 = df.to_numpy()                         # b2 = 10 kpl


# oletan että kuva on muotoa 28*28 koska 28*28=784 ja tiedostossa on 784 riviä
print(kuva.reshape(28,28))
plt.figure(1)
plt.imshow(kuva.reshape(28,28))
plt.show()

def sigmd(arr):
	return np.divide(arr, 20)

rarr = np.linspace(-20, 20, 100)
sarr = sigmd(rarr)
print(rarr)
print(sarr)
plt.figure(2)
plt.plot(rarr, sarr)
plt.show()



def doNeuro(w1, w2, b1, b2, data):
	layer1 = np.add(sigmd(np.matmul(w1, data)), b1)
#	print(layer1)
	layer2 = np.add(sigmd(np.matmul(w2, layer1)), b2)
#	print(layer2)
	return layer2

print(doNeuro(w1, w2, b1, b2, kuva))