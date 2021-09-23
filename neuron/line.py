import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')
MATH = data['math score'].values.reshape(-1,1)
READ = data['reading score'].values.reshape(-1,1)
plt.scatter(MATH, READ)
plt.show()

lin_reg = LinearRegression()
lin_reg.fit(MATH, READ)
MATH_pred = lin_reg.predict(MATH)
plt.plot(MATH, MATH_pred, color = "red")
plt.show()

lin_reg.fit(READ, MATH)
READ_pred = lin_reg.predict(READ)
plt.plot(READ, READ_pred, color = "yellow")
plt.show()

order = np.argsort(MATH.ravel())
plt.plot(MATH[order], READ_pred[order])
plt.show()