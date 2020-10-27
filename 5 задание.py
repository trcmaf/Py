a = input("Введите сторону А >> ")
b = input("Введите сторону B >> ")
c = input("Введите сторону C >> ")
m = input("Введите M(высота двери) >> ")
k = input("Введите К(ширина двери) >> ")

if (b <= k and a <= m) or (c <= k and a <= m) or (a <= k and b <= m) or (c <= k and b <= m) or (a <= k and c <= m) or (b <= k and c <= m):
    print("Коробка пройдет в дверь")
else:
    print("Коробка не пройдет в дверь")



