x = float(input("Введите число >> "))
a = float(input("Введите первую границу >> "))
b = float(input("Введите вторую границу >> "))
if a > x > b:
    print("Число принадлежит промежутку")
elif a < x < b:
    print("Число принадлежит промежутку")
else:
    print("Число не принадлежит промежутку")
