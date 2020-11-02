N = int(input("Введите количество элементов >> "))
a = [[0]*N for i in range(N)]
for i in range(N):
    a[i] = float(input("Введите элемент массива >> "))
summ = sum(a)
pol = 0
print("Сумма элементов >> ", summ)
for i in range(N):
    if a[i] >= 0:
        pol += 1
print("Количество положительных элементов >> ", pol)
a.insert(0, summ)
a.insert(1, pol)
print(a)
