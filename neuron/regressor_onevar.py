import pickle
import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
import matplotlib.pyplot as plt

input_file = 'regressor_onevar.txt'

data = np.loadtxt(input_file, delimiter = ',')
X, y = data[:, :-1], data[:, -1]

num_training = int(0.8 * len(X))
num_test = len(X) - num_training
X_train, y_train = X[:num_training], y[:num_training]
X_test, y_test = X[num_training:], y[num_training:]

#creating a linear regressor
regressor = linear_model.LinearRegression()
#training
regressor.fit(X_train, y_train)
#PREDICTION
y_test_pred = regressor.predict(X_test)

#Graph
plt.scatter(X_test, y_test, color = 'green')
plt.plot(X_test, y_test_pred, color = 'black', linewidth = 4)
plt.xticks(())
plt.yticks(())
plt.show()

#metrics
print ("Linear regressor perfomance: ")
print ("Mean absolute error = ", round(sm.mean_absolute_error(y_test, y_test_pred), 2))
print ("Mean squared error = ", round(sm.mean_squared_error(y_test, y_test_pred), 2))
print ("Median absolute error = ", round(sm.median_absolute_error(y_test, y_test_pred), 2))
print ("Explain variance score = ", round(sm.explained_variance_score(y_test, y_test_pred), 2))
print ("R2 score = ", round(sm.r2_score(y_test, y_test_pred), 2))

#saving the model
output_model_file = 'model.pkl'
with open(output_model_file, 'wb') as f:
    pickle.dump(regressor, f)

#loading model file
with open(output_model_file, 'rb') as f:
    regressor_model = pickle.load(f)

#getting prediction
y_test_pred_new = regressor_model.predict(X_test)
print ("\nNew mean absolute error = ", round(sm.mean_absolute_error(y_test, y_test_pred_new), 2))