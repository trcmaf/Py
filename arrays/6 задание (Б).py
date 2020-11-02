N = int(input("Введите количество элементов >> "))
M = int(input("Введите M >> "))
K = int(input("Введите число К >> "))
P = int(input("Введите число P >> "))
a = [[0]*N for i in range(N)]
for i in range(N):
    a[i] = float(input("Введите элемент массива >> "))
a[K:M+K+1], a[P:M+P+1] = a[P:M+P+1], a[K:M+K+1]
print(a)
