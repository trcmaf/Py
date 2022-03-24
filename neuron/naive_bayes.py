import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection

from utilities import visualize_classifier

input_file = 'data_multivar_nb.txt'
data = np.loadtxt(input_file, delimiter=',')
X, Y = data[:, :-1], data[:, -1]

#Creation of naive bayes classifier
classifier = GaussianNB()

#learning
classifier.fit(X, Y)
#TEST Prediction
y_pred = classifier.predict(X)

#Accuracy of classifier
accuracy = 100.0 * (Y == y_pred).sum() / X.shape[0]
print ("Accuracy of Naive Bayes classifier = ", round(accuracy, 2), " %")
#Visualization of classifier
visualize_classifier(classifier, X, Y)

#NEW CLASSIFIER
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=3)
classifier_new = GaussianNB()
classifier_new.fit(X_train, Y_train)
Y_test_pred = classifier_new.predict(X_test)
accuracy = 100.0 * (Y_test == Y_test_pred).sum() / X_test.shape[0]
print ("Accuracy of the new classifier = ", round(accuracy, 2), " %")
visualize_classifier(classifier_new, X_test, Y_test)

#Accuracy, precision, recall
num_folds = 3
accuracy_values = model_selection.cross_val_score(classifier, X, Y, scoring='accuracy', cv = num_folds)
print ("Accuracy = " + str(round(100 * accuracy_values.mean(), 2)) + " %")

precision_values = model_selection.cross_val_score(classifier, X, Y, scoring='precision_weighted', cv = num_folds)
print ("Precision = " + str(round(100 * precision_values.mean(), 2)) + " %")

recall_values = model_selection.cross_val_score(classifier, X, Y, scoring='recall_weighted', cv = num_folds)
print ("Recall = " + str(round(100 * recall_values.mean(), 2)) + " %")

f1_values = model_selection.cross_val_score(classifier, X, Y, scoring='f1_weighted', cv = num_folds)
print ("F1 = " + str(round(100 * f1_values.mean(), 2)) + " %")