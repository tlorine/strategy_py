import random

for i in range(5):
    random.seed(i)  # даёт каждый раз одинаковые результаты
    print(i, [random.randint(1, 3)
                    for i in range(10)])