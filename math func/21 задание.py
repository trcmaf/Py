import math
a = float(input("Введите А >> "))
if a <= 0:
    def f(x):
        f = 0
        return f
    print(f(a))
elif 0 < a <= 1:
    def f(x):
        f = x**2 - x
        return f
    print(f(a))
else:
    def f(x):
        f = x**2 - math.sin(math.pi*x**2)
        return f
    print(f(a))
    
    
