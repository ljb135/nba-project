from numpy import *
from pandas import *
import csv


csv_filename = "training_data.csv"
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')  # load the dataset

# split into input (X) and output (y) variables
X = dataset[:, 1:417]
y = dataset[:, 417]
