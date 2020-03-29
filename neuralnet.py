from numpy import *
from pandas import *
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
import csv


def train(train_csv_filename, excluded):
    train_dataset = loadtxt(train_csv_filename, delimiter=',')

    # split into input (X) and output (Y) variables
    X = train_dataset[:, 2:444 - (26*excluded)]
    Y = train_dataset[:, 0]

    model = Sequential()
    model.add(Dense(64, input_dim=442 - (26*excluded), activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.fit(X, Y, epochs=400, batch_size=64)
    return model


def test(model, test_csv_filename, excluded):
    test_dataset = loadtxt(test_csv_filename, delimiter=',')

    x = test_dataset[:, 2:444 - (26*excluded)]
    y = test_dataset[:, 0]

    print(model.evaluate(x, y))


def predict(model, predict_csv_filename, excluded):
    predict_dataset = loadtxt(predict_csv_filename, delimiter=',')

    x = predict_dataset[:, 2:444 - (26 * excluded)]
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
        if prediction[x][0] == int(data[x][443]):
            print(str(x+1) + ")", prediction[x][0], data[x][443], "correct")
            num_correct += 1
        else:
            print(str(x + 1) + ")", prediction[x][0], data[x][443], "incorrect")
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


neural_net = train("training_data.csv", 0)
test(neural_net, "testing_data.csv", 0)
predict(neural_net, "predict_data.csv", 0)
# neural_net.save_weights("model_weights.h5")

# print(model.predict(x))
# weights = model.get_weights()
# print(weights)



# _, accuracy = model.evaluate(x, y)
# print('Accuracy: %.2f' % (accuracy*100))
# validation_data=(x, y)