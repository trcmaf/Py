import pickle
import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
import matplotlib.pyplot as plt

input_file = 'regressor_onevar.txt'

data = np.loadtxt(input_file, delimeter = ',')
X, y = data[:, :-1], data[:, -1]

