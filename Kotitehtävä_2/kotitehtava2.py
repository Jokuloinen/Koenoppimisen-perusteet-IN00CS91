import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#""" 
#Tehtävä 1: 
#- lataa Latest https://covidtracking.com/data/download/national-history.csv
#  tiedosto pandas kirjaston avulla Pandas dataframeksi. 
#- "Irroita" siitä ladattaessa'date','deaths','hospitalInc','hospitalNow' sarakkeet
#- Piirrä matplotlib.pyplot kirjaston ja plt.subplot, plt.plot, plt.title, plt.show 
#  komentojen avulla kuva, josta nähdään kuolleiden lukumäärät, sairaalapotilaiden
#  inkrementaalinen kasvu ja kuinka paljon sairaalassa on potilaita eri päivinä.
#- Selvitä minä päivänä potilaiden kasvu on ollut suurinta ja mikä on tuon päivän potilasmäärä
#"""
# load file
#curl https://covidtracking.com/data/download/national-history.csv > in.csv
# url = "https://covidtracking.com/data/download/national-history.csv"
url = "in.csv" # gives a 403 for some reason when using a real url
data = pd.read_csv(url)
subData0 = data.date
subData1 = data.death
subData2 = data.hospitalizedIncrease
subData3 = data.hospitalizedCurrently
# print(data)

print(len(data))

plt.figure(1)
plt.subplot(311)
plt.plot(subData1, "-b")
plt.subplot(312)
plt.plot(subData2, "-b")
plt.subplot(313)
plt.plot(subData3, "-b")
#plt.show()

#data.iloc[::-1]
#data.reindex(index=data.index[::-1])
#print(subData1.head)





#"""
#Tehtävä 2:
#- Muuta kaikki dataFramen sarakkeet numpy arrayksi to_numpy() funktion avulla
#- Tulosta kuolleiden määrä ja sairaalassa olleiden lukumäärät oikeassa järjestyksessä
#  (huom päivämäärät ovat tiedostossa viimeisin päivämäärä ensin. Eli käännä tulostusjärjestys
#   siten, että kuvaan tulostetaan deaths sarakkeen viimeisin alkio ensin jne.)
#""" 



reSubData0 = subData0.to_numpy();
reSubData1 = subData1.to_numpy();
reSubData2 = subData2.to_numpy();
reSubData3 = subData3.to_numpy();




plt.figure(2)
plt.subplot(311)
plt.plot(reSubData1[::-1], "-b")
plt.subplot(312)
plt.plot(reSubData2[::-1], "-b")
plt.subplot(313)
plt.plot(reSubData3[::-1], "-b")
plt.show()