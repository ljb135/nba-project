from numpy import *
from pandas import *
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.python.client import device_lib
import csv


train_csv_filename = "training_data.csv"
test_csv_filename = "testing_data.csv"

train_dataset = loadtxt(train_csv_filename, delimiter=',')  # load the dataset
test_dataset = loadtxt(test_csv_filename, delimiter=',')

# split into input (X) and output (y) variables
X = train_dataset[:, 1:417]
y = train_dataset[:, 417]

model = Sequential()
model.add(Dense(12, input_dim=416, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, epochs=400, batch_size=10)

X = test_dataset[:, 1:417]
y = test_dataset[:, 417]

_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
