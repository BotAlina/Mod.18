n = int(input("Сколько мест забронировать? "))
print("Укажите возраст посетителя")
s = 0
for i in range(n):
    age = int(input("Возраст: "))
    if age < 18:
        s += 0
    elif 18 <= age < 25:
        s += 990
    else:
        s += 1390
if n > 3:
    f = 0.9
    print("Итого со скидкой -", s * f)
else:
    f = 1
    print("Итого", s * f)