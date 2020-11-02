from array import *
N = int(input("Введите количество элементов >> "))
a = []
for i in range(N):
    a.append(float(input("Введите элемент массива >> ")))

res = list(filter(None, a))
print(res)
