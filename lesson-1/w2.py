def f(x):
    x = x if len(x) == 2 else f'0{x}'
    if len(x) > 2:
        x = str(int(x)%24)
        x = f(x[-2:])
    return x

time = -1
while time < 0:
    time = int(input("Ввведите время в секундах: "))
s = str(time%60)
s = f(s)
m = str((time//60)%60)
m = f(m)
h = str(time//3600)
h = f(h)
print(f"Время в формате чч:мм:сс - {h}:{m}:{s}")