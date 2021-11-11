from math import *
import os 

os.system('cls') or None

a = int(input("Insert the value of incognita 'a': "))
b = int(input("Insert the value of incognita 'b': "))
c = int(input("Insert the value of incognita 'c': "))

delta = (pow(b,2)) - (4 * a * c)

x1 = (-b + sqrt(delta)) / (2 * a)
x2 = (-b - sqrt(delta)) / (2 * a)

if (delta == 0):
    print("x1 = x2 =", x1)
else:
    print("x1 = ", x1, "\nx2 = ", x2)