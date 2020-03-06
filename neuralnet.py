from numpy import *
from pandas import *
import csv


# reads data from csv file3
def read_csv_file(filename):
    data_matrix = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data_matrix.append(row)
    return data_matrix


csv_filename = "training_data.csv"
orig_csv_data = read_csv_file(csv_filename)
print(DataFrame(orig_csv_data))