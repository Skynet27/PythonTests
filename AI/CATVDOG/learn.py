import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
import matplotlib.pyplot as plt
import numpy as np
import random
import pickle
import cv2
import os

DATADIR = "../datasets/PetImages/"
CATEGORIES = ["Dog","Cat"]

TRAINING_DATA = []
img_size = 50

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR,category) #Elérési út összekötése a képekhez
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (img_size, img_size))
                TRAINING_DATA.append([new_array, class_num])
            except:
                pass

create_training_data()
#print(len(TRAINING_DATA))

random.shuffle(TRAINING_DATA)
for sample in TRAINING_DATA[:10]:
    print(sample[1])

x = []
y = []

for features, label in TRAINING_DATA:
    x.append(features)
    y.append(label)

x = np.array(x).reshape(-1, img_size, img_size, 1)

pickle_out = open("x.pickle","wb")
pickle.dump(x, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()

print("\n\nDone with the analyzing.")

#adatbetöltés és mentés készen van.
