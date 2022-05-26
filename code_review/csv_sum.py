import csv as c

with open("data.csv", encoding='utf-8') as data:
    obj = c.reader(data, delimiter=",")
    obj = [item for item in obj]
    print(sum(list(map(int, obj[0]))) == 10)






# Скрипт использует встоенную библиотеку языка для уменьшения количества устанавливемых пакетов.
# Библиотека Pandas избыточна для такой задачи