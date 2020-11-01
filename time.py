import datetime
a = int(input("Вы хотите вывести дату? 1 - да, 0 - нет >> "))
b = int(input("Вы хотите вывести время? 1 - да, 0 - нет >> "))
now = datetime.datetime.now()
if a == 1 and b == 1:
    print (now)
elif a == 1 and b == 0:
    print (now.year,"-", now.month,"-", now.day)
elif a == 0 and b == 1:
    print (now.hour,":", now.minute,":", now.second,":", now.microsecond)

