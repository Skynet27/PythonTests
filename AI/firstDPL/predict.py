import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

mnist = tf.keras.datasets.mnist #28x28 kézzel írott számok 0-9
(x_train, y_train), (x_test, y_test) = mnist.load_data() #adatbetöltés
x_train = tf.keras.utils.normalize(x_train, axis=1) #normalizálás
x_test = tf.keras.utils.normalize(x_test, axis=1)

new_model = tf.keras.models.load_model('number_15EPs.model') #betölti a régi modelt


predictions = new_model.predict(x_test) #csinál egy meghatározást

print(np.argmax(predictions[150]))
plt.imshow(x_test[150], cmap = plt.cm.binary)
plt.show()

print(np.argmax(predictions[100]))
plt.imshow(x_test[100], cmap = plt.cm.binary)
plt.show()

print(np.argmax(predictions[270]))
plt.imshow(x_test[270], cmap = plt.cm.binary)
plt.show()
