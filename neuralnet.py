from numpy import *
from pandas import *
from keras.models import Sequential
from keras.layers import Dense
import csv


csv_filename = "training_data.csv"
dataset = loadtxt(csv_filename, delimiter=',')  # load the dataset

# split into input (X) and output (y) variables
X = dataset[:, 1:417]
y = dataset[:, 417]

print(y)

model = Sequential()
model.add(Dense(12, input_dim=416, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, epochs=150, batch_size=10)

_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
