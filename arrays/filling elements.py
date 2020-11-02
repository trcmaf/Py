a = []
N = int(input("Введите количество элементов >> "))
for i in range(N):
    a.append(int(input("Введите элемент массива >> ")))
for i in range(1, N, 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(a)
    
