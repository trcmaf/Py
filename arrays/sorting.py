N = int(input("Введите количество элементов >> "))
if N % 2 != 0:
    print("Количество элементов должно быть четным")
    N = int(input("Введите количество элементов >> "))
a = [[0] * N for i in range(N)]
for i in range(N):
    a[i] = float(input("Введите число >> "))
for i in range(N//2):
    b = a[i]
    a[i] = a[N//2+i]
    a[N//2+i] = b
for j in range(N):
    print(a[j])      
