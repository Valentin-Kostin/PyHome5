# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def degree_num(a, b):
    if b == 0:
        return 1
    return a*degree_num(a, b-1)


numA = int(input('введите чисело А: '))
numB = int(input('введите чисело B: '))

print(degree_num(numA, numB))
