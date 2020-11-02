a = []
N = int(input("Введите количество элементов >> "))
for i in range(N):
    a.append(int(input("Введите элемент массива >> ")))
temp=0
for i in range (N-1):
    temp = a[i]
    a[i] = a[i+1]
    a[i+1] = temp
   
print(a)
    
