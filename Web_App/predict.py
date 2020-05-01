from keras.models import load_model
from numpy import *


def calc_min_ratio(input):
    total_min = sum(input[0:546:21])
    for i in range(0, 26):
        input[i*21] = input[i*21]/total_min
    return input


def run_model(stat_list):
    stat_list = calc_min_ratio(stat_list)
    model = load_model('model.h5')
    prediction = model.predict(stat_list)
    if prediction < 0.5:
        return "Away Team Wins"
    else:
        return "Home Team Wins"
