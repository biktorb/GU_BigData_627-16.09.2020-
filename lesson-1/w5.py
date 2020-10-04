proceeds = int(input("Введите выручку фирмы :"))
costs = int(input("Введите издержки фирмы : "))
if costs > proceeds:
    print("К сожалению ваша фирма работает в убыток.")
else:
    print("Ваша фирма работает с прибылью.")
    plus = (proceeds - costs)
    rent = plus / proceeds
    print(f"Рентабильность вашей фирмы - {rent}")
    count = int(input("Введите кол-во сотрудников в фирме"))
    pr_w = plus / count
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет - {pr_w}")