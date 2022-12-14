# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

Ax = int(input("Введите координату точки Ax :"))
Ay = int(input("Введите координату точки Ay :"))

Bx = int(input("Введите координату точки Bx :"))
By = int(input("Введите координату точки By :"))

def distance_between_coordinates(Ax,Ay,Bx,By):
    distance = round((((Bx - Ax) ** 2) + ((By - Ay) ** 2)) ** 0.5, 2)
    return distance
print(f'Расстояние между координатами [{Ax}, {Ay}] и [{Bx}, {By}] равняется:'
      f' \n {distance_between_coordinates(Ax, Ay, Bx,By)}')
