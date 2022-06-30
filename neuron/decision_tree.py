import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier

from utilities import visualize_classifier

input_file = 'decision_tree_data.txt'
data = np.loadtxt(input_file, delimiter=',')
X, y = data[:, :-1], data[:, -1]

class_0 = np.array(X[y == 0])
class_1 = np.array(X(y == 1))

#VISUALIZATION
plt.figure()
plt.scatter(class_0[:, 0], class_1[:, 1], s = 75, c = 'black', linewidths = 1, marker = 'x')
plt.scatter(class_1[:, 0], class_1[:, 1], s = 75, c = 'white', linewidths = 1, marker = 'o')
plt.title('Входные данные')

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = 0.25, random_state = 5)
