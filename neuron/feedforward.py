import numpy as np

def sigmoid(x):
    # функция активации: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        # Вводные данные о весе, добавление смещения и последующее использование функции активации
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)

#weights = np.array([0, 1])  # w1 = 0, w2 = 1
w1 = int(input("Enter w1 >> "))
w2 = int(input("Enter w2 >> "))
weights = np.array([w1, w2])
bias = 4  # b = 4
n = Neuron(weights, bias)

#x = np.array([2, 3])  # x1 = 2, x2 = 3
x1 = int(input("Enter x1 >> "))
x2 = int(input("Enter x2 >> "))
x = np.array([x1, x2])

print(n.feedforward(x))  # 0.9990889488055994

