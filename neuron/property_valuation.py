import numpy as np
import sklearn.metrics as sm
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsOneClassifier
from sklearn import model_selection

from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.svm import SVR

data = datasets.load_boston()
X, y = shuffle(data.data, data.target, random_state = 7)
