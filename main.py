from math import sqrt
import sys


def InterValue():
    a = float(input("a = "))
    if a == 0:
        print("Якщо а = 0, це не квадратнє рівняння")
        InterValue()
        return
    b = float(input("b = "))
    c = float(input("c = "))
    return Solve(a, b, c)

def NInter():
    a, b, c = NInterValue()
    if a == 0:
        print("Якщо а = 0, це не квадратнє рівняння")
        NInter()
        return
    Solve(a, b, c)


def NInterValue():
    file = open("a,b,c.txt", "r")
    values = file.read()
    result_value = []
    try:
        for item in values.split():
            result_value.append(float(item))
    except:
        print("Неправильні дані")
        sys.exit(1)
    return result_value

def Solve(a, b, c):
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
            InterValue()
            quit()
        elif _input == 2:
            NInter()
            quit()
        elif _input == 3:
            quit()
        elif print("Будь ласка введіть потрібну опцію меню"):
            continue
