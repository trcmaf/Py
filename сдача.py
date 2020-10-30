a = int(input("Сколько у вас денег? "))
cf = 0
co = 0
cte = 0
ctw = 0
while (a>=500):
    a = a - 500
    cf += 1
while (a>=100):
    a = a - 100
    co += 1
while (a>=10):
    a = a - 10
    cte += 1
while (a>=2):
    a = a - 2
    ctw += 1
print("Купюр по 500: ",cf)
print("Купюр по 100: ",co)
print("Монет по 10: ",cte)
print("Монет по 2: ",ctw)
print("Осталось: ",a)

