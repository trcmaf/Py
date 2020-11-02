N = int(input("Введите количество элементов >> "))
a = [[0]*N for i in range(N)]
M = int(input("Введите M >> "))
b = [[0]*M for i in range(M)]
K = int(input("Введите K >> "))
for i in range(N):
    a[i] = float(input("Введите элемент массива A >> "))
for i in range(M):
    b[i] = float(input("Введите элемент массива B >> "))
a.insert(K, b)
print(a)
