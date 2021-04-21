from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
from keras.datasets import mnist
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import cv2

WEIGHT = 500
HEIGHT = 400
# Load the data and split it in train and test sets
(X_test, y_test), (X_train, y_train) = mnist.load_data()

# Print the shape
print(X_test.shape)


# Reshape
X_train = X_train.reshape(
    X_train.shape[0], X_train.shape[1], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[1], 1)
print(f"new shape {X_test.shape}")

# Normalize the data between 0-1
X_test = X_test/255
X_train = X_train/255

# One hot encoding for the labels
y_test_encoded = to_categorical(y_test)
y_train_encoded = to_categorical(y_train)


# Build CNN model
model = Sequential()
# Add the layers
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy'])

print("Model compiled succesfully..")
model.summary()

# Train the mmodel
hist = model.fit(X_train, y_train_encoded,
                 validation_data=(X_test, y_test_encoded), epochs=3)
print("Model trained succesfully..")

score = model.evaluate(X_test, y_test_encoded, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# Save the model
model.save('trained_model.h5')
print("Model saved succesfully..")
