__author__ = 'Lenovo'

import codecs
import numpy as np
from numpy.random import randint
from numpy import argmax

import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.models import model_from_json
from keras.preprocessing import image
from keras.optimizers import SGD
from keras.models import load_model

model = load_model(r"image_classificator_CNN_with_augmentation.h5")

classes = ['first_class_image', 'second_class_image']


img_path = r"PATH/TO/INPUT/IMAGE/name.{}.jpg"
img = image.load_img(img_path, target_size=(150,150))
plt.imshow(img)
plt.show()

x = image.img_to_array(img)
x /= 255
x = np.expand_dims(x, axis = 0)

#from keras.utils.np_utils import to_categorical

prediction = model.predict(x)


#prediction = argmax(np_utils.to_categorical(prediction, num_classes=2), axis=1)
k = model.predict_classes(x)
#print(classes[prediction[0]])
#print(prediction)
print(classes[k[0]])