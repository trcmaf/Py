year = int(input("Введите год >> "))

if year%4 == 0 or (year%100 == 0 and year%400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")

def vek(year):
    vek = year//100 + 1
    return vek

print("Век - ", vek(year))
