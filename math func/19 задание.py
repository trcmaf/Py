a = float(input("Введите А >> "))

if a <= 2:
    def f(x):
        f = x**2 + 4*x + 5
        return f
    print(f(a))
else:
    def f(x):
        f = 1/(x**2 + 4*x + 5)
        return f
    print(f(a))
