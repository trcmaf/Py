a = []
j = int(input("Введите количество элементов >> "))
for i in range(j):
    a.append(int(input("Введите элемент массива >> ")))
temp=0
for i in range (j-1):
    temp = a[i]
    a[i] = a[i+1]
    a[i+1] = temp
   
print(a)
    
