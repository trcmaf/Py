a = float(input("Введите число а >> "))
b = float(input("Введите число b >> "))
c = float(input("Введите число c >> "))
d = float(input("Введите число d >> "))
if (a < c and b < d) or (a < d and b < c) or (b < c and a < d) or (b < d and a < c):
    print("Прямоуголник поместится внутри другого")
else:
    print("Прямоуголник не поместится внутри другого")
