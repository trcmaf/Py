import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


x = np.array([2,4,10,12,20,25,26,34,38]).reshape((-1,1))
y = np.array([3,6,7,15,25,20,17,10,7,]).reshape((-1,1))

model = LinearRegression()
model.fit(x,np.ravel(y.astype(int)))
plt.scatter(x,y)
plt.show()
print(model.score(x,y))