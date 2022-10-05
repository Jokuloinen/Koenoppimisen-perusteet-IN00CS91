'''

Toteuta alla olevan esimerkin mukainen CNN käsinkirjoitettujen numeroiden tunnistamiseksi

https://keras.io/examples/vision/mnist_convnet/

 

Sen lisäksi, että kopioit pitkälti toteutuksen yllä olevasta linkistä tee seuraavat tehtävät:

 

Prepare the data kohdassa:
Tulosta y_train ennen vektori luokkien konvertointia binääriksiksi ja konvertoinnin jälkeen. Konvertoinnin jälkeinen tuloshan on konvoluutioverkon odotettu oikea tulos. Miksi tulos on juuri tuollainen?
Build the model kohdasssa:
Selitä, miksi yksi suodatus tarkoittaa 10 säädettävää parametria. Ensimmäinen suodatus käsittää 32 suodatinta ja säädettäviä parametreja tuossa vaiheessa on 320 eli yhdessä suodattimessa pitää sitten olla 10 säädettävää parametria, mutta mitkä nuo parametrit ovat?
	3*3 array parametreja ja biassi
Selitä, miksi ensimmäisen suodatuksen Conv2D jälkeen kuvan koko pienenee 28*28 kuvasta 26*26 kuvaksi.
	nimensä mukaan suodatus prosessi vähentää tietoa
Selitä, miksi kuvan koko puolittuu edellen MaxPooling 2D kuvassa.
	suodatusprosessi kai on onnistuneesti suodattanut tärkeimmät ominaisuudet kuvasta jota käyttää seraavassa vaiheessa
Selitä, mistä tulevat toisen suodatuksen säädettävien parametrien luvut
	?? kai tää tekoäly opettaa ne itselleen
Selitä, mistä tulee fully connected layerin säädettävien parametrien lukumäärät.
	neuronien biassien määrästä
Tee koodi, jonka avulla voit löytää 60000 kuvan joukosta ne kuvat, joita CNN ei kykene tunnistamaan oikein.
Ja palauta tähän tehtävään google colabissa tekemäsi koodi.
'''
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# Load the data and split it between train and test sets
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print("ytrain", y_train)

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")


# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
print("ytrain", y_train)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.summary()

batch_size = 128
epochs = 15

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

pred_y = model.predict(x_test)
rped_y = np.round(pred_y, 0).astype(int)

print(pred_y.astype(int), pred_y.shape, pred_y[0].shape)
print(y_test.astype(int), y_test.shape, y_test[0].shape)
print(rped_y[0:15], "\t", y_test[0:15])

failed_lst = []
for i in range(0, rped_y.shape[0]):
  pushval = 0
  for ii in range(0, 10):
    if rped_y[i, ii] != y_test[i, ii]:
      pushval += 1
  if pushval != 0:
    failed_lst.append(i)

print("failed test on following input indecies:\n", failed_lst)
print(len(failed_lst), "\n", y_test.shape)