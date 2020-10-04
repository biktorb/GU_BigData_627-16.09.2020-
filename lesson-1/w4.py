n = input("Введите целое положительное число: ")
max = 0
while n:
    i = int(n[0])
    if i > max:
        max = i
    n = n[1:]
print(f"Самая большая цифра в числе - {max}")