import sklearn.metrics as sm
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.svm import SVR

data = datasets.load_boston()
X, y = shuffle(data.data, data.target, random_state = 7)

num_training = int(0.8 * len(X))
X_train, y_train = X[:num_training], y[:num_training]
X_test, y_test = X[num_training:], y[num_training:]

#creating linear model based on SVM
sv_regressor = SVR(kernel = 'linear', C = 1.0, epsilon = 0.1)

sv_regressor.fit(X_train, y_train)

y_test_pred = sv_regressor.predict(X_test)
print ("Mean absolute error = ", round(sm.mean_absolute_error(y_test, y_test_pred), 2))
print ("Median absolute error = ", round(sm.median_absolute_error(y_test, y_test_pred), 2))
print ("Mean squared error = ", round(sm.mean_squared_error(y_test, y_test_pred), 2))
print ("Explained variance score = ", round(sm. explained_variance_score(y_test, y_test_pred), 2))
print ("R2 score = ", round(sm.r2_score(y_test, y_test_pred), 2))

#test datapoint
test_data = [3.7, 0, 18.4, 1, 0.87, 5.95, 91, 2.5052, 26, 666, 20.2, 351.34, 15.27]
print ("Predicted price = ", sv_regressor.predict([test_data])[0])
