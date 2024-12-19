import math


def square(side):
    side = math.ceil(side)
    area = side ** 2
    return area


side = float(input("Введите длину стороны квадрата: "))
area = square(side)
print(f"Площадь квадрата: {area}")
