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
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

#data = pd.read_csv("dataout.csv", index_col=["x"], delimiter="\t", header=0, usecols=['x', 'y', 'z', 'labels'])
data = pd.read_csv("dataout.csv",
delimiter="\t",
header=None,
usecols=[1,2,3,4]
#names = ['x','y','z','labels']
)
data = data[1:-1]
data = data[data[1].astype(int) < 1024]
data = data[data[2].astype(int) < 1024]
data = data[data[3].astype(int) < 1024]

#categ = data[4].as_type(catgory)
data[5] = data[4].astype('category').cat.codes;
nData = data[[1,2,3]].astype(int).to_numpy();
nLabe = data[[5]].to_numpy();
print(nData)
print(nLabe)

x_train, x_test, y_train, y_test = train_test_split( nData, nLabe, test_size=0.2, random_state=0)
print(x_train, x_test)
print(y_train, y_test)


model = RandomForestClassifier(n_estimators=40, n_jobs=8)
model.fit(x_train, y_train.ravel())
#RandomForestClassifier(bootstrap=true, class_weight=None, criterion='gini', max_depth=None, max_features='auto', max_leaf_nodes=None, min_impurity_split=1e-07, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, n_estimators=40, n_jobs=1, oob_score=False, random_state=None, verbose=0, warm_start=False)
print(model.score(x_test, y_test))
y_pred = model.predict(x_test)
print(confusion_matrix(y_test, y_pred))


k_range = range(1,26)
scores = {}
scores_lst = []
for k in k_range:
	knn = KNeighborsClassifier(n_neighbors=k)
	knn.fit(x_train, y_train.ravel())
	y_pred2=knn.predict(x_test)
	scores[k]= metrics.accuracy_score(y_test, y_pred2)
	scores_lst.append(metrics.accuracy_score(y_test, y_pred2))
	print(confusion_matrix(y_test, y_pred2))
print(scores)
print(scores_lst)


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