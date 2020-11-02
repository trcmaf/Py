N = int(input("Введите количество элементов >> "))
M = int(input("Введите М >> "))
K = int(input("Введите К >> "))
a = [[0]*N for i in range(N)]
for i in range(N):
    a[i] = float(input("Введите элемент массива >> "))
a[K:K+M] = []
print(a)
