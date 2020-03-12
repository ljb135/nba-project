from numpy import *
from pandas import *
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense


def read_data(train_csv_filename):
    data = loadtxt(train_csv_filename, delimiter=',')
    d_list = []
    for i in range(1, 27):
        d_list.append(i * 16 - 1)
        d_list.append(i * 16)
    data = delete(data, d_list, 1)
    return data


def train(train_csv_filename, excluded):
    train_dataset = read_data(train_csv_filename)

    # split into input (X) and output (Y) variables
    X = train_dataset[:, 1:417 - (26*excluded)]
    Y = train_dataset[:, 417 - (26*excluded)]

    model = Sequential()
    model.add(Dense(16, input_dim=416 - (26*excluded), activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.fit(X, Y, epochs=300, batch_size=32)
    return model


def test(model, test_csv_filename, excluded):
    test_dataset = read_data(test_csv_filename)

    x = test_dataset[:, 1:417 - (26*excluded)]
    y = test_dataset[:, 417 - (26*excluded)]

    print(model.evaluate(x, y))


# print(read_data("training_data.csv")[0])

neural_net = train("training_data.csv", 2)
test(neural_net, "19-20_data.csv", 2)
neural_net.save_weights("model_weights.h5")

# print(model.predict(x))
# weights = model.get_weights()
# print(weights)



# _, accuracy = model.evaluate(x, y)
# print('Accuracy: %.2f' % (accuracy*100))
# validation_data=(x, y)