# Kotitehtävä 1

Kari Jyrkkä


## Tehtävät

### Tehtävä 1:

Käy läpi Eeron luentomateriaali ja suorita sen materiaalin tehtäviä läpi. Käy läpi myös annetut `pythonPerusteet_datatyypit.py` ja `pythonPerusteet_rakenteet.py` tiedostot. Tee python skripti tiedosto, jossa luot lista, tuple, set ja dictionary muuttujat. Laita jokaiseen muuttujaan 3 elementtiä ja tulosta print komennolla niistä keskimmäinen eli toinen alkio.

### Tehtävä 2:

Tee python skripti tiedosto, joka luo ensin tyhjän listan ja tuohon tyhjään listaan lisätään toistorakenteessa aina jokaisella toistorakenteen ”kierroksella” uusi luku ja tulostetaan listan arvo jokaisella kierroksella. Näin pitäisi saada syntymään viereisen kuvan mukainen tulostus.

```
[2]
[2, 3]
[2, 3, 4
[2, 3, 4, 5]
[2, 3, 4, 5, 6]
[2, 3, 4, 5, 6, 7]
[2, 3, 4, 5, 6, 7, 8]
[2, 3, 4, 5, 6, 7, 8, 9]
```

## Tehtävät jatkuu

### Tehtävä 3:

Saat annettuna `tehtava1.py` nimisen tiedoston, jossa on toteutettuna eräs luokka. Tee seuraavat tehtävät:

1. Selitä mitä tapahtuu riveillä, joissa on kommentti #mitä tässä tapahtuu? Eli tutustu numpy modulin arange, zeros, cos, sin metodeihin numpyn dokumentaation avulla.

2. Lisää luokkaan toiminto, jolla voit tulostaa kosinisignaalin lisäksi sini signaalin. Eli muuta create ja plot metodeja siten, että create muodostaa myös sini signaalin ja plot metodi tulostaa matplotlib.pyplot subplot funktion avulla kaksi kuvaa. Toiseen kosinin ja toiseen sinin.

3. Toteuta vielä toinen python scripti, jonka nimeksi `signalGenerator.py`, joka käyttää `tehtava1.py` skriptiä modulina, josta se importtaa signalAnalyser luokan. Tee `signalGenerator.py` tiedostosta sellainen, että käytäjä voi antaa signaalin taajuuden ja aika-akselin pituuden ja sen jälkeen piirretään vaaditun mittainen ja vaaditun taajuinen sini- ja kosini signaali `tehtava1.py` modulin signalAnalyser luokkaa hyödyntäen. Oleta, että näytetaajuus Fs = 1000 Hz ja muista, että tällöin käyttäjä voi antaa taajuusarvon vain väliltä 0 – 500 Hz. Katso seuraavalta kalvolta miltä ohjelman suorituksen pitäisi näyttää…

![](Kotitehtävä1/tehtävänannot/esimerkki_kuva.png)