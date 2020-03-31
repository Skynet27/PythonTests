import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import TensorBoard
import numpy as np
import pickle
import time

gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpus[0],True)


pickle_in = open("x.pickle", "rb")
x = pickle.load(pickle_in)
x = np.array(x)

pickle_in = open("y.pickle", "rb")
y = pickle.load(pickle_in) # megnyitjuk az előző adatokat
y = np.array(y)

x = x/255.0

dense_layers = [0, 1, 2]
layer_sizes = [32, 64]
conv_layers = [1, 2, 3]

for dense_layer in dense_layers:
    for layer_size in layer_sizes:
        for conv_layer in conv_layers:
            name = f"{dense_layer}-dense-{layer_size}-size-{conv_layer}-convlayers--{int(time.time())}"
            tensorboard = TensorBoard(log_dir='logs/{}'.format(name))

            model = Sequential()
            model.add(Conv2D(layer_size, (3, 3), input_shape=x.shape[1:]))
            model.add(Activation('relu'))
            model.add(MaxPooling2D(pool_size=(2, 2)))

            for l in range(conv_layer-1):
                model = Sequential()
                model.add(Conv2D(layer_size, (3, 3)))
                model.add(Activation('relu'))
                model.add(MaxPooling2D(pool_size=(2, 2)))

            model.add(Flatten())

            for l in range(dense_layer):
                model.add(Dense(layer_size))
                model.add(Activation('relu'))

            model.add(Dense(1))
            model.add(Activation('sigmoid'))

            model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

            model.fit(x, y, validation_split=0.3, batch_size=32, epochs=20, callbacks=[tensorboard])
            tf.keras.backend.clear_session()
            model = None
            tensorboard = None
            # model.save('CATVDOG.model')
