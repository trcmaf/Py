a = float(input("Введите первое число >> "))
b = float(input("Введите второе число >> "))
c = float(input("Введите третье число >> "))
if a < b < c:
    print("Выполняется неравенство ",a,"<",b,"<",c)
elif a >= b >= c:
    print("Выполняется неравенство ",a,">=",b,">=",c)
else:
    print("Не выполняется ни одно из неравенств")
