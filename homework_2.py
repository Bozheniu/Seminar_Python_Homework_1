# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# (расшифровка этого выражения not (x[0] or y[1] or z[2]) = not x[0] and not y[1] and not z[2])
# для всех значений предикат.

def numbers(x):
    x_y_z = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {x_y_z[i]}: "))
    return a


def checking(x):
    side_left = not (x[0] or x[1] or x[2])
    side_right = not x[0] and not x[1] and not x[2]
    result = side_left == side_right
    return result


statement = numbers(3)

if checking(statement) == True :
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")