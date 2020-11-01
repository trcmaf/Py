import math

x = float(input("Введите Х >> "))
y = float(input("Введите Y >> "))

if x > y:
    z = math.sqrt(x*y)
    print("Z = ", z)
else:
    z = math.log(x + y)
    print("Z = ", z)
