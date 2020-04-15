from numpy import *
from pandas import *
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from keras.layers import Dropout
from keras.constraints import maxnorm
import csv
import matplotlib.pyplot as plt


def train(train_csv_filename):
    train_dataset = loadtxt(train_csv_filename, delimiter=',')

    # split into input (X) and output (Y) variables
    X = train_dataset[:, 2:]
    Y = train_dataset[:, 1]

    model = Sequential()
    # model.add(Dense(84, input_dim=546, activation='relu'))
    # model.add(Dense(16, activation='relu'))
    # model.add(Dense(4, activation='relu'))
    # model.add(Dense(1, activation='sigmoid'))
    model.add(Dense(64, input_dim=546, activation='relu', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.1))
    model.add(Dense(16, activation='relu', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.1))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.fit(X, Y, epochs=400, batch_size=64)
    return model


def analyze_train(train_csv_filename, test_csv_filename):
    train_dataset = loadtxt(train_csv_filename, delimiter=',')
    test_dataset = loadtxt(test_csv_filename, delimiter=',')

    # split into input (X) and output (Y) variables
    x_train = train_dataset[:, 2:]
    y_train = train_dataset[:, 1]

    x_test = test_dataset[:, 2:]
    y_test = test_dataset[:, 1]

    model = Sequential()
    model.add(Dense(256, input_dim=546, activation='relu', kernel_constraint=maxnorm(3)))
    model.add(Dropout(0.25))
    # model.add(Dense(64, activation='relu', kernel_constraint=maxnorm(3)))
    # model.add(Dropout(0.1))
    model.add(Dense(1, activation='sigmoid'))

    # model.add(Dense(64, input_dim=546, activation='relu'))
    # model.add(Dense(16, activation='relu'))
    # model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    history = model.fit(x_train, y_train, epochs=50, batch_size=128, validation_data=(x_test, y_test), verbose=1)
    print(model.evaluate(x_test, y_test))

    # graph training vs. validation accuracy over epochs
    plt.figure(1)
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')

    # graph training vs. validation loss over epochs
    plt.figure(2)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

    return model


def test(model, test_csv_filename):
    test_dataset = loadtxt(test_csv_filename, delimiter=',')

    x = test_dataset[:, 2:]
    y = test_dataset[:, 1]

    print(model.evaluate(x, y))


def predict(model, predict_csv_filename):
    predict_dataset = loadtxt(predict_csv_filename, delimiter=',')

    x = predict_dataset[:, 2:]
    prediction = model.predict(x)

    data = read_csv_file(predict_csv_filename)
    num_correct = 0
    total = 0

    for i in range(len(prediction)):
        if prediction[i] <= 0.5:
            prediction[i] = 0
        else:
            prediction[i] = 1
    for x in range(len(data)):
        if prediction[x][0] == int(data[x][1]):
            print(str(x+1) + ")", prediction[x][0], data[x][1], "correct")
            num_correct += 1
        else:
            print(str(x + 1) + ")", prediction[x][0], data[x][1], "incorrect")
        total += 1
    accuracy = num_correct/total
    print("Accuracy: " + str(accuracy))


def read_csv_file(filename):
    data_matrix = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data_matrix.append(row)
    return data_matrix


neural_net = analyze_train("training_data.csv", "testing_data.csv")
# test(neural_net, "testing_data.csv")
# stats_excluded = 0
# neural_net = train("training_data.csv")
# test(neural_net, "testing_data.csv")
# predict(neural_net, "predict_data.csv")
# neural_net.save_weights("model_weights.h5")

# print(model.predict(x))
# weights = model.get_weights()
# print(weights)
# _, accuracy = model.evaluate(x, y)
# print('Accuracy: %.2f' % (accuracy*100))
# validation_data=(x, y)