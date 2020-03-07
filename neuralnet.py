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

# split into input (X) and output (Y) variables
X = train_dataset[:, 1:417]
Y = train_dataset[:, 417]

x = test_dataset[:, 1:417]
y = test_dataset[:, 417]

model = Sequential()
model.add(Dense(200, input_dim=416, activation='relu'))
# model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, Y, epochs=75, batch_size=50)
# print(model.predict(x))
weights = model.get_weights()
print(weights)
# print(model.evaluate(x, y))


# _, accuracy = model.evaluate(x, y)
# print('Accuracy: %.2f' % (accuracy*100))
# validation_data=(x, y)