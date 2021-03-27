from sys import *
import random

# 19.03

# DATA READING

# file1 = open('test.txt', encoding='utf-8')
# lines = file1.read()
# # file1.close()
# print(lines)
# print(type(lines))
# file1.seek(0)
#
# file1 = open('test.txt', encoding='utf-8')
# lines2 = file1.readlines()
# # file1.close()
# print(lines2)
# file1.seek(0)
#
# # GET RID OF '\n' AT THE END OF LINES
#
# # file1 = open('test.txt', encoding='utf-8')
# lines3 = file1.read() .splitlines()
# file1.close()
# print(lines3)
#
# with open('test.txt') as f:
#     for lo in f:
#         print(lo, end="")

# DATA WRITING

# print("Enter the data you want to save to the file: ")
# data = stdin.readline()
# file2 = open('test1.txt', 'w+', encoding='utf-8')
# file2.write(data)
# file2.close()
# list1 = []
# for x in range(6):
#     list1 += [x]
# file2 = open('test1.txt', 'a+', encoding='utf-8')
# # a+ - adding data
# file2.writelines(str(list1))
# file2.close

# OBJECT ORIENTED PROGRAMMING - INTRODUCTION

# class defining


# class FirstClass:
#     """First class in python - empty"""
#     attribute1 = 911
#
#     def first_method(self):
#         return "Now first method is working"
#
#
# FirstObject = FirstClass()
# print(FirstObject)
# print(FirstObject.attribute1)
# print(FirstObject.first_method())
# FirstObject.text = "Text"    # text is only for this object
# print(FirstObject.text)
# # SecondObject = FirstObject()
# # print(SecondObject.text)

# constructor

# class Shapes:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.description = "Class for general shapes"
#
#     def area(self):
#         return self.x * self.y
#
#     def circuit(self):
#         return 2 * self.x + 2 * self.y
#
#     def add_description(self, text):
#         self.description = text
#
#     def scaling(self, factor):
#         self.x *= factor
#         self.y *= factor
#
#
# square = Shapes(20, 20)
# print((square.area()))
# print(square.circuit())
# square.add_description("This is square")
# print(square.description)
# square.scaling(0.5)
# print(square.x)
# print(square.y)

# HOMEWORK

# 1

# list1 = [x for x in range(31)]
# list1 = [x * 2 for x in list1]
# task1file = open("Task1.txt", 'w')
# task1file.writelines(str(list1))
# task1file.close()

# 2

# task1file = open("Task1.txt", 'r')
# lines1 = task1file.read()
# task1file.close()
# print(lines1)

# 3

# print("Enter text: ")
# text = stdin.readlines()
#
# with open('Task3.txt', 'a+') as file:
#     file.writelines(str(text))
#
# with open('Task3.txt') as file:
#     for lines in file:
#         print(lines, end="")

# 4

# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyswietl_produkt(self):
#         print("Produkt to %(z1)s w cenie %(z3)f/%(z2)s" %{"z1":self.nazwa_produktu,
#                                                           "z2":self.jednostka_miary,
#                                                           "z3":self.cena_jed})
#
#     def ile_produktu(self):
#         print(str(self.ilosc) + " " + str(self.jednostka_miary))
#
#     def ile_kosztuje(self):
#         stdout.write("Produkt w tej ilosci kosztuje ")
#         return self.ilosc * self.cena_jed
#
#
# potatoes = NaZakupy("Ziemniaki", 10, "kg", 1.4)
# print(potatoes.wyswietl_produkt())
# print((potatoes.ile_produktu()))
# print((potatoes.ile_kosztuje()))

# 5

# class CiagArytm:
#     a1 = 0
#     r = 0
#     n = 0
#     elementy_ciagu = []
#
#     def wyswietl_dane(self):
#         print("Pierwszy element ciagu to ", self.a1, ", roznica = ", self.r, " a ilosc elementow wynosi ", self.n)
#
#     def pobierz_elementy(self, wartosc, miejsce_w_ciagu):
#         self.elementy_ciagu[miejsce_w_ciagu - 1] = wartosc
#         print(self.elementy_ciagu)
#
#     def pobierz_parametry(self):
#         print("Podaj parametry.")
#         self.a1 = input("Pierwszy element ciagu: ")
#         self.r = input("Roznica ciagu: ")
#         self.n = input("Ilosc elementow ciagu: ")
#
#     def policz_sume(self):
#         self.a1 = float(self.a1)
#         self.r = float(self.r)
#         self.n = int(self.n)
#         return (((2 * self.a1) + (self.n - 1) * self.r) * self.n) / 2
#
#     def policz_elementy(self):
#         self.a1 = float(self.a1)
#         self.r = float(self.r)
#         self.n = int(self.n)
#         self.elementy_ciagu = [self.a1 + (x - 1) * self.r for x in range(1, self.n + 1, 1)]
#         print(self.elementy_ciagu)
#
#
# ciag = CiagArytm()
# ciag.pobierz_parametry()
# ciag.wyswietl_dane()
# print(ciag.policz_sume())
# ciag.policz_elementy()
# ciag.pobierz_elementy(1, 7)

# 6

# class Robaczek:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.krok = 1
#
#     def idz_w_gore(self, ile_krokow):
#         self.y = self.y + self.krok * ile_krokow
#
#     def idz_w_dol(self, ile_krokow):
#         self.y = self.y - self.krok * ile_krokow
#
#     def idz_w_lewo(self, ile_krokow):
#         self.x = self.x - self.krok * ile_krokow
#
#     def idz_w_prawo(self, ile_krokow):
#         self.x = self.x + self.krok * ile_krokow
#
#     def pokaz_gdzie_jestes(self):
#         print("Aktualna pozyca to x = ", self.x, ", y = ",self.y)
#
#
# robak = Robaczek(0, 0)
# robak.idz_w_gore(10)
# robak.idz_w_prawo(5)
# robak.pokaz_gdzie_jestes()
# robak.idz_w_dol(11)
# robak.idz_w_lewo(9)
# robak.pokaz_gdzie_jestes()

