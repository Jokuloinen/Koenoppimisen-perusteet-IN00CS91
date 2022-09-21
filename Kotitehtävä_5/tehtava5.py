'''
Install scikit-learn module with pip install scikit-learn command.

Tehtävät:
1. Luetaan dataout.csv tiedosto pandas data frameksi siten, että tiedostosta luetaan vai
   sarakkeet xyz ja labels. Eli jätetään se indeksi sarake, joka koostuu 0,1,2 jonosta pois. 
   Käytä dataframen read_csv funktiota ja sieltä parametreja delimiter=, header=, usecols=

2. Poistetaan edellä luetusta dataframesta sen ensimmäinen rivi, jossa siis xyz ja labels tieto.
   Tämä siksi, että jäljelle jäänyttä 60,3 matriisia ja string saraketta käytetään eri algoritmien
   opettamiseen. Käytä dataframe iloc metodia

3. Seuraavaksi suodatetaan dataframesta pois sellaiset rivit, joissa x,y tai z arvo on suurempi
   kuin 1023, mikä on Arduinon analogia muuntimen maksimi lukema. Eli poistetaan virheelliset 
   mittaustulokset. Tulosta dataframe rivistä 40 eteenpäin (iloc käsky) ennen suodatusta ja 
   suodatuksen jälkeen, jotta varmistut siitä, että osa riveistä poistuu suodatuksen avulla
   Selvitä internetin avulla kuinka pandas dataframen sarakkeen arvoja voi suodattaa.

4. Seuraavaksi irroitetaan dataframesta labels tiedot left, right, up ja down tietoja
   kertova sarake (sen pitäisi olla neljäs sarake. Voit kokeilla esim print(df[4]) komennolla)
   Muutetaan sarakkeen tyyppi as_type komennolla 'category' tyypiksi ja luodaan dataframeen
   vielä viides sarake ja alustetaan sinne df[4].cat.codes funktion avulla numeeriset arvot
   left, rigth, up ja down arvoja vastaamaan.

5. Seuraavaksi "irroitetaan" dataframesta x,y,z sarakkeet ja muodostetaan niistä yksi 
   NumPy array, jossa on kolme saraketta ja N kpl rivejä. Tämä array = matriisi = data on sitten
   se, mitä käytetään eri mallien datana opettamiseen. Irroitetaan myös numpy arrayksi
   se viides sarake joka edellisessä vaiheessa saatiin tehtyä. Ja tätä käytetään opetuksessa
   kertomaan, mitä kukin data matriisin rivi edustaa = labels. Ja muutetaan molemmat irroitetut
   data ja labels int tyyppisiksi.

6. Ja nyt vihdoin data on käsitelty algoritmin opettamiseen sopivaksi. Jaetaan data vielä
   training ja test datasetteihin ja käytetään siihen sklearn kirjaston train_test_split luokkaa
   jonka voi importata komennolla from sklearn.model_selection import train_test_split. Tee
   sellainen jako, että datasta 20% jätetään testaukseen ja 80% datasta käytetään opetukseen.
   Netistä löytyy taas hyviä esimerkkejä, miten tämä tehtään: https://realpython.com/train-test-split-python-data/

7. Ja lopuksi testataan random forest ja K-means algoritmien toimivuutta. Eli opetetaan opetusdatalla
   x_train,y_train sekä random forest että K-means malli. Ja sen jälkeen testataan mallin tarkkuus
   x_test,y_test datalla. Ja ylimääräisenä tehtävänä voi vielä mitata kummastakin algoritmista kuinka
   kauaan mallin opettaminen kestää ja kuinka kauan yhden ennustuksen tekeminen mallilla kestää. Ja
   apuja löytyy taas netistä seuraavasti:
   K-means: https://towardsdatascience.com/knn-using-scikit-learn-c6bed765be75
   Random Forests:https://www.datacamp.com/tutorial/random-forests-classifier-python

       
'''

import sklearn # This is anyway how package is imported
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

data = pd.read_csv("dataout.csv", index_col=["x"], delimiter="\t", header=0, usecols=['x', 'y', 'z', 'labels'])
print(data)



# 7x³+5x²+6x+17
# 21x²+10x+6


# (3x²+5x+12)³
# 3(3x²+5x+12)²*(6x+5)


# a²*2x³+b⁵*x²+c*x+10
# 2a*15x²5b⁴*2x+c

# fa 2x³a
# fb 5x²b⁴
# fc x
# fx 3a²*x²+2b²*x+c