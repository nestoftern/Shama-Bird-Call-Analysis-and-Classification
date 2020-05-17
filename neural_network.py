import sys
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.xception import Xception, preprocess_input
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report, roc_curve
from sklearn.preprocessing import LabelBinarizer
from sklearn.utils import class_weight
import keras
from keras import backend as K
from keras.models import Sequential, Model
from keras.layers import Input,Dense, Dropout, Activation, Flatten, Convolution2D, Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers.core import Dropout
from keras.layers.normalization import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.regularizers import l2
from keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt



model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(64, 64, 3)))
#model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Dropout(0.25))
model.add(Flatten())
#model.add(Dense(64, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(4, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())



early_stopping = EarlyStopping(monitor='val_loss', patience=50, verbose=1)
callbacks = [early_stopping]

train_datagen = ImageDataGenerator(preprocessing_function = preprocess_input,  
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   shear_range=0.2,
                                   zoom_range=0.1,
                                   fill_mode='nearest',
                                   horizontal_flip = False)
test_datagen = ImageDataGenerator(preprocessing_function = preprocess_input)

training_set = train_datagen.flow_from_directory('../TERN/Bird Call Analysis/bird call data/train',
                                                 target_size = (64, 64),
                                                 batch_size = 16,
                                                 class_mode = 'categorical', shuffle=True)

test_set = test_datagen.flow_from_directory('../TERN/Bird Call Analysis/bird call data/test',
                                            target_size = (64, 64),
                                            batch_size = 16,
                                            class_mode = 'categorical')

val_set = test_datagen.flow_from_directory('../TERN/Bird Call Analysis/bird call data/val',
                                            target_size = (64, 64),
                                            batch_size = 16,
                                            class_mode = 'categorical')

class_weights = class_weight.compute_class_weight(
               'balanced',
                np.unique(training_set.classes), 
                training_set.classes)

model.fit_generator(training_set, epochs=10, class_weight=class_weights,  validation_data = test_set, verbose=True, callbacks=callbacks, shuffle=True)

model.save('Model_birdclass.h5')

Y_pred = model.predict_generator(val_set)
y_pred = np.argmax(Y_pred, axis=1)

print(classification_report(val_set.classes, y_pred))

score = model.evaluate_generator(training_set, verbose=0)
print("Training Accuracy: ", score[1])

score = model.evaluate_generator(test_set, verbose=0)
print("Testing Accuracy: ", score[1])

score = model.evaluate_generator(val_set, verbose=0)
print("Validating Accuracy: ", score[1])




'''
from keras.preprocessing import image
img_width, img_height = 64, 64

# load the model we saved
# Get test image ready
test_image = image.load_img('../TERN/Bird Call Analysis/data/Koel.png', target_size=(img_width, img_height))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)

result = model.predict(test_image, batch_size=1)
print(result)
img_class=model.predict_classes(test_image) 
prediction = img_class[0]
classname = img_class[0]
print("Class: ",prediction)
'''
