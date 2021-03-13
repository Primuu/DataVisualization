from teksty import *
from ciagi import *
from sys import *
import random

# 11.04

# Python comprehension
# Example No1
# A={x^2: x ∈ <0,9>}
# B={1,3,9,27,...,3^10}
# C={x: x∈A & x=2k+1, k∈Z}'

# loop examples

# a = []
#
# for x in range(10):
#     a.append(x ** 2)
# print(a)
#
# b = []
#
# for x in range(11):
#     b.append(3 ** x)
# print(b)
#
# c = []
#
# for x in a:
#     if x % 2 == 1:
#         c.append(x)
# print(c)
#
# list_d = []
#
# for i in [1, 2, 3]:
#     for j in [4, 5, 6]:
#         list_d.append((i, j))
# print(list_d)

# Python comprehension examples

# aa = [x ** 2 for x in range(10)]
# print(aa)
#
# bb = [3 ** x for x in range(11)]
# print(bb)
#
# cc = [x for x in a if x % 2 == 1]
# print(cc)
#
# list_dd = [(i, j) for i in [1, 2, 3] for j in [4, 5, 6]]
# print(list_dd)

# Key changing (dictionary)

# dic = {"key1": "value1",
#        "key2": "value2",
#        "key3": "value3"}
#
# changed = {}
#
# for k, v in dic.items():
#     changed[v] = k
# print(changed)
#
# changed2 = {v: k for k, v in dic.items()}
# print(changed2)

# Functions
# Quadratic equation

# def qua_eq (a = 2, b = 8, c = -10):
#     delta = b ** 2 - 4 * a * c
#     if a != 0:
#         if delta > 0:
#             x1 = -b - sqrt(delta) / 2 * a
#             x2 = -b + sqrt(delta) / 2 * a
#             return x1, x2
#         elif delta == 0:
#             x = -b / 2 * a
#             return x
#         else:
#             stdout.write("There is no solution ")
#             return -1
#     else:
#         x = -c / b
#         stdout.write("It's not a quadratic equation x =")
#         return x
#
# print(qua_eq())
# print(qua_eq(6, 1, 3))
# print(qua_eq(1, 2, 1))
# print(qua_eq(1, 4, 1))
# print(qua_eq(0, 4, 2))

# * - any number of arguments

# def sequence (* numbers):
#     if len(numbers) == 0:
#         return 0
#     else:
#         ssum = 0
#         for i in numbers:
#             ssum += i
#         return ssum
#
# print(sequence())
# print(sequence(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# * - any numbers of arguments with key

# def sth (** m):
#     for x in m:
#         stdout.write(x)
#         print(" ", m[x])
#
#
# print(sth(top1="Mount Everest", top2="Aconcagua"))

# Import

# a = "Sentence"
# litery.wyswietl(a)
# print(litery.dlugosc(a))
#
# print(dir(litery))
#
# print(piosenka.zespol())
# print(piosenka.spiew())

# HOMEWORK

# 1

# a = [1 - x for x in range(1, 11, 1)]
# print(a)
#
# b = [4 ** x for x in range(8)]
# print(b)
#
# c = [x for x in b if x % 2 == 0]
# print(c)

# 2

# list1 = [random.randrange(0, 1000000000) for x in range(10)]
# print(list1)
#
# list2 = [x for x in list1 if x % 2 == 0]
# print(list2)

# 3

# groceries = {"eggs": "egg insert",
#              "milk": "carton",
#              "bread": "loaf",
#              "apples": "kilograms",
#              "ham": "decagrams"}
#
# print(groceries)
#
# changed_groceries = {k: random.randrange(0, 30) for k, v in groceries.items()}
# print(changed_groceries)

# 4


# def is_triangle(a, b, c):
#     if max(a, b, c) - min(a, b, c) < (a + b + c) - max(a, b, c) - min(a, b, c):
#         if (a * a + b * b == c * c) | (a * a + c * c == b * b) | (b * b + c * c == a * a):
#             print("It's a right triangle. ")
#         else:
#             print("It's not a right triangle.")
#     else:
#         print("It cannot be triangle.")
#
#
# print(is_triangle(4, 5, 3))
# print(is_triangle(6, 5, 3))
# print(is_triangle(5, 1, 2))

# 5

# def trapezoid_area(a = 2, b = 1, h = 4):
#     area = a + b * h / 2
#     return area
#
# print(trapezoid_area())
# print(trapezoid_area(8, 2, 2))

# 6 ???????????????????????????????????????????

# def product_seq(a1 = 1, b = 4, ile = 10):
#     product = a1
#     for x in range(ile):
#         a2 = a1 * b
#         product *= a2
#         a1 = a2
#     return product
#
#
# print(product_seq(2, 2, 10))

# 7 ???????????????????????????????????????????

# def product_seq1(* a):
#     if len(a) == 0:
#         return 0
#     else:
#         product = 1
#         for x in a:
#             product *= x
#         return product
#
#
# print(product_seq1(4, 3, 2, 8, 9))

# 8

# # shopping_list = {"eggs": 12.50,
# #                  "milk": 2.59,
# #                  "bread": 1.99,
# #                  "apples": 3.99,
# #                  "ham": 18.99}
#
#
# def value_s(** m):
#     quantity = 0
#     worth = 0
#     for x, y in m.items():
#         y = float(y)
#         quantity += 1
#         worth += y
#     print("Produkty " + str(quantity) + "\n Wartosc " + str(worth))
#
#
# print(value_s(eggs="12.50", milk="2.59", bread="1.99", apples="3.99", ham="18.99"))

# 9

# print(arytm.n_ty_wyraz_a(1, 2, 100))
# print(arytm.suma_n_wyrazow_a(1, 100, 100))
# print(geo.n_ty_wyraz_g(1, 2, 10))
# print(geo.suma_n_wyrazow_g(1, 2, 10))
