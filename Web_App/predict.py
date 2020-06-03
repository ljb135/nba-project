from keras.models import load_model
from numpy import *


def mod_min_ratio(home_stats, away_stats):
    edit_stat_indexes = [4, 5, 7, 9, 11, 12, 13, 14, 15, 16, 17, 18]

    home_total_min = sum(home_stats[0:273:21])
    home_min_ratio = 5*48/home_total_min
    for i in range(0, 13):
        for j in edit_stat_indexes:
            home_stats[i*21+j] = round(home_stats[i*21+j] * home_min_ratio, 1)

    away_total_min = sum(away_stats[0:273:21])
    away_min_ratio = 5*48/away_total_min
    for i in range(0, 13):
        for j in edit_stat_indexes:
            away_stats[i*21+j] = round(away_stats[i*21+j] * away_min_ratio, 1)

    return home_stats + away_stats


def run_model(home_stats, away_stats):
    print(home_stats, away_stats)
    full_list = mod_min_ratio(home_stats, away_stats)
    print(full_list)
    print(len(full_list))
    # model = load_model('model.h5')
    # prediction = model.predict(full_list)
    # if prediction < 0.5:
    #     return "Away Team Wins"
    # else:
    #     return "Home Team Wins"
