from math import sqrt
import sys



def InterSolve():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print(f"({a}) x^2 + ({b}) x + ({c}) = 0")
    d = pow(b, 2) - (4 * a * c)
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print("Це рівняння має 2 рішення")
        print(f"x1 = {x1}, x2 = {x2}")
    elif d == 0:
        x1 = -(b / (2 * a))
        print("Це рівняння має 1 рішення")
        print(f"x = {x1}")
    else:
        print("Це рівняння немає рішень")


if __name__ == "__main__":
    while True:
        _input = int(
            input("Виберіть режим калькулятора: \n1.Інтерактивний\n2.Не Інтерактивний\n3.Завершити програму\n>"))
        if _input == 1:
            InterSolve()
            quit()
        elif _input == 3:
            quit()
        elif print("Будь ласка введіть потрібну опцію меню"):
            continue
