x = float(input("Введите Х >> "))
y = float(input("Введите Y >> "))
z = float(input("Введите Z >> "))

if (x < y + z) and (y < x + z) and (z < x + y):
    print("Треугольник существует")
    if (x**2 == y**2 + z**2) or (y**2 == x**2 + z**2) or (z**2 ==x**2 + y**2):
        print("Треугольник прямоугольный")
    else:
        print("Треугольник не прямоугольный")
else:
    print("Треугольник не существует")
