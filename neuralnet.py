from numpy import *
from pandas import *
from keras.models import Sequential
from keras.layers import Dense


def train(train_csv_filename):
    train_dataset = loadtxt(train_csv_filename, delimiter=',')  # load the dataset

    # split into input (X) and output (Y) variables
    X = train_dataset[:, 1:417]
    Y = train_dataset[:, 417]

    model = Sequential()
    model.add(Dense(12, input_dim=416, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.fit(X, Y, epochs=400, batch_size=10)
    return model


def test(model, test_csv_filename):
    test_dataset = loadtxt(test_csv_filename, delimiter=',')

    x = test_dataset[:, 1:417]
    y = test_dataset[:, 417]

    print(model.evaluate(x, y))


neural_net = train("18-19_data.csv")
test(neural_net, "17-18_data.csv")

# print(model.predict(x))
# weights = model.get_weights()
# print(weights)



# _, accuracy = model.evaluate(x, y)
# print('Accuracy: %.2f' % (accuracy*100))
# validation_data=(x, y)