from sys import *

# 25.03

# Class inheritance


# class Shapes:
#
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
# # The class that inherits from class "Shapes"
#
#
# class Square(Shapes):
#
#     def __init__(self, x):
#         self.x = x
#         self.y = x
#
#
# # The class that inherits from class "Square"
# # Square "L"
# #  _
# # | |_
# # |_ _|
#
#
# class SquareL(Square):
#
#     def circuit(self):
#         return 8 * self.x
#
#     def __str__(self):
#         return "Square with side equal to ()".format(self.x)
#
#     def area(self):
#         return 3 * self.x * self.x
#
#
# rectangle = Shapes(5, 10)
#
# print(rectangle.area())
# print(rectangle.circuit())
#
# square = Square(9)
#
# print(square.area())
# print(square.circuit())
# square.add_description("Square")
# print(square.description)
# print(square)
#
# squareL = SquareL(10)
#
# print(squareL.circuit())
# print(squareL.area())
# print(squareL)

# Global


# class Point:
#
#     counter = []
#
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
#
#     def update(self, n):
#         self.counter.append(n)
#
#
# p1 = Point(0, 0)
# p2 = Point(1, 1)
#
# print(p1.counter)
# print(p2.counter)
# p1.update(1)
# print(p1.counter)
# print(p2.counter)

# "Empty" class (similar to structure in C), Global attribute


# class Employee:
#     pass
#
#
# John = Employee()
# John.name = "John"
# John.surname = "Smith"
# John.age = 30
#
# print(John.age)


# class Employee1:
#
#     __private__ = "secret password"
#
#     def __init__(self, name):
#         self.name = name
#
#
# John = Employee1("John")
#
# print(John.__private__)

# Inheritance #2


# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def introduce_yourself(self):
#         return "I'm {} {}".format(self.name, self.surname)
#
#
# class Employee2(Person):
#
#     def __init__(self, name, surname, salary):
#         Person.__init__(self, name, surname)
#         # or
#         # super().__init__(name, surname)
#         self.salary = salary
#
#     def introduce_yourself(self):
#         return "I'm {} {}, I earn {}".format(self.name, self.surname, self.salary)
#
#
# class Manager(Employee2):
#
#     def introduce_yourself(self):
#         return "I'm Manager, my name is {} {}. I earn {}".format(self.name, self.surname, self.salary)
#
#
# Joseph = Employee2("Joseph", "Tale", 2000)
# Romeo = Manager("Romeo", "Julietowsky", 8000)
#
# print(Joseph.introduce_yourself())
# print(Romeo.introduce_yourself())

# OR LIKE THAT # # # # # # # # # # # # # # # # # # # # # # # # #


# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def introduce_yourself(self):
#         return "I'm {} {}".format(self.name, self.surname)
#
#
# class Employee2():
#
#     def __init__(self, salary):
#         self.salary = salary
#
#     def introduce_yourself(self):
#         return "I'm {} {}, I earn {}".format(self.name, self.surname, self.salary)
#
#
# class Manager(Person, Employee2):
#
#     def __init__(self, name, surname, salary):
#         Person.__init__(self, name, surname)
#         Employee2.__init__(self, salary)
#
#     def introduce_yourself(self):
#         return "I'm Manager, my name is {} {}. I earn {}".format(self.name, self.surname, self.salary)
#
#
# Romeo = Manager("Romeo", "Julietowsky", 8000)
#
# print(Romeo.introduce_yourself())

# Iterator and generator

# for x in range(1, 11):
#     print(x)

# Example1

# name = "John"
# it = iter(name)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))  # error

# Example2

# class Backwards:
#     """Iterator returning values in backward order"""
#
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
#
#
# example = Backwards("123456789")
# print(example.__next__())
# print(example.__next__())
# print(example.__next__())
# print(example.__next__())
# print(example.__next__())

# Example3

# def reverse(data):
#     for index in range(len(data) - 1, -1, -1):
#         yield data[index]
#
#
# gen = reverse("Phoenix")
# print(next(gen))
# print("STH")
# print(next(gen))

# Example4

# letters = (letter for letter in "James")
# print(letters)
# print(next(letters))

# HOMEWORK

# 1

# class Material:
#     def __init__(self, rodzaj, dlugosc, szerokosc):
#         self.rodzaj = rodzaj
#         self.dlugosc = dlugosc
#         self. szerokosc = szerokosc
#
#     def wyswietl_nazwe(self):
#         print(self.rodzaj)
#
#
# class Ubrania(Material):
#     def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo):
#         super().__init__(rodzaj, dlugosc, szerokosc)
#         self.rozmiar = rozmiar
#         self.kolor = kolor
#         self.dla_kogo = dla_kogo
#
#     def wyswietl_dane(self):
#         print("Ubranie wykonane z {} o dlugosci {}, szerokosci {} (w rozmiarze {}), w kolorze {} dla {}".format(self.rodzaj,
#                                                                                                      self.dlugosc,
#                                                                                                      self.szerokosc,
#                                                                                                      self.rozmiar,
#                                                                                                      self.kolor,
#                                                                                                      self.dla_kogo))
#
#
# class Sweter(Ubrania):
#     def __init__(self, rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo, rodzaj_swetra):
#         super().__init__(rodzaj, dlugosc, szerokosc, rozmiar, kolor, dla_kogo)
#         self.rodzaj_swetra = rodzaj_swetra
#
#
#     def wyswietl_dane(self):
#         print("Sweter typu {} wykonany z {} o dlugosci {}, szerokosci {} (w rozmiarze {}), w kolorze {} dla {}".format(
#             self.rodzaj_swetra,
#             self.rodzaj,
#             self.dlugosc,
#             self.szerokosc,
#             self.rozmiar,
#             self.kolor,
#             self.dla_kogo))
#
#
# bawelna = Material("bawelna", "10 m", "5 m ")
#
# bawelna.wyswietl_nazwe()
#
# bluza = Ubrania("bawelna", "70 cm", "52 cm", "L", "czarny", "mezczyzn")
#
# bluza.wyswietl_nazwe()
# bluza.wyswietl_dane()
#
# sweter = Sweter("welna", "82 cm", "56 cm", "M", "bialy", "kobiet", "rozpianany")
#
# sweter.wyswietl_nazwe()
# sweter.wyswietl_dane()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# class Shapes:
#
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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 2


# class Square(Shapes):
#
#     def __init__(self, x):
#         self.x = x
#         self.y = x
#
#     def __add__(self):
#         new = self.x + 4 * self.x
#         return new
#
#     def __str__(self):
#         return "{}".format(self.x)
#
#
# kwadrat = Square(5)
# kwadrat1 = Square(kwadrat.__add__())
# print(kwadrat1)

# 3


# class Square(Shapes):
#
#     def __init__(self, x):
#         self.x = x
#         self.y = x
#
#     def __ge__(self, other):
#         return (self.x >= other.x)
#
#     def __gt__(self, other):
#         return (self.x > other.x)
#
#     def __lt__(self, other):
#         return  (self.x < other.x)
#
#     def __le__(self, other):
#         return  (self.x <= other.x)
#
# kwadratd = Square(5)
# kwadratm = Square(3)
#
# print(kwadratm.__ge__(kwadratd))
# print(kwadratd.__gt__(kwadratm))
# print(kwadratm.__le__(kwadratd))
# print(kwadratd.__lt__(kwadratm))

# 4


# class Point:
#
#     counter = []
#
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
#
#     def update(self, n):
#         self.counter.append(n)
#
#
# p1 = Point(1, 0)
# p2 = Point(1, 2)
# p3 = Point(3, 0)
# p4 = Point(4, 1)
#
# p1.update(1)
# p2.update(3)
# p3.update(6)
# p4.update(8)
#
# print(p1.counter)
# print("")
# print(p2.counter)
# print("")
#
# p3.counter.pop()
# print(p1.counter)

# 5


# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def introduce_yourself(self):
#         return "I'm {} {}".format(self.name, self.surname)
#
#
# class Employee2(Person):
#
#     def __init__(self, name, surname, salary):
#         Person.__init__(self, name, surname)
#         # or
#         # super().__init__(name, surname)
#         self.salary = salary
#
#     def introduce_yourself(self):
#         return "I'm {} {}, I earn {}".format(self.name, self.surname, self.salary)
#
#
# class Manager(Employee2):
#
#     def introduce_yourself(self):
#         return "I'm Manager, my name is {} {}. I earn {}".format(self.name, self.surname, self.salary)
#
#
# Pracownik = Employee2("John", "Babel", 3000)
# Manadzer = Manager("Karolina", "Wojtylowsky", 21370)
#
# print(isinstance(Pracownik, Person))
# print(isinstance(Pracownik, Employee2))
# print(isinstance(Pracownik, Manager))
# print(isinstance(Manadzer, Person))
# print(isinstance(Manadzer, Employee2))
# print(isinstance(Manadzer, Manager))
#
# print("\n", issubclass(Person, Person))
# print(issubclass(Person, Employee2))
# print(issubclass(Person, Manager))
# print(issubclass(Employee2, Person))
# print(issubclass(Employee2, Employee2))
# print(issubclass(Employee2, Manager))
# print(issubclass(Manager, Person))
# print(issubclass(Manager, Employee2))
# print(issubclass(Manager, Manager))

# 6


# class Backwards:
#     """Iterator returning values in backward order"""
#
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
#
#
# example1 = Backwards("123456789")
#
# print(example1.__next__())
# print(example1.__next__())
# print(example1.__next__())
# print(example1.__next__())
# print(example1.__next__())
#
# example2 = Backwards(["a", "b", "c", "d"])
#
# print(example2.__next__())
# print(example2.__next__())
# print(example2.__next__())
# print(example2.__next__())

# 7


# class TylkoParzyste:
#
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == len(self.data)-1:
#             raise StopIteration
#         elif self.index % 2 == 0:
#             self.index += 1
#             return self.data[self.index]
#         else:
#             self.index += 1
#
#
# example1 = TylkoParzyste("123456789")
#
# print(example1.__next__())
# print(example1.__next__())
# print(example1.__next__())
# print(example1.__next__())
# print(example1.__next__())

# 8


# class Samogloski:
#
#     def __init__(self, data):
#         self.data = data
#         self.index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if isinstance(self.data, str):
#             if self.index == len(self.data) - 1:
#                 raise StopIteration
#             self.index = self.index + 1
#             if self.data[self.index] in "aąeęiouy":
#                 return self.data[self.index]
#         else:
#             raise StopIteration
#
#
#
# lista = ["aaaa"]
# napis = 'sprawdzamy działanie'
# obiekt = Samogloski(napis)
# obiekt1 = Samogloski(lista)
#
# for a in obiekt:
#     print (a)
#
# for a in obiekt1:
#     print(a)

# 9

# def tylkoparzyste(data):
#     for x in range(0, len(data), 1):
#         if data[x] % 2 == 0:
#             yield data[x]
#
# example = tylkoparzyste([1, 2, 3, 4, 5, 6])
#
# print(next(example))
# print(next(example))
# print(next(example))

# 10

# def ciag(a1, r, n):
#     for x in range(1, n+1, 1):
#         an = a1 + (x - 1) * r
#         yield an
#
#
# ciag = ciag(1, 1, 10)
#
# print(next(ciag))
# print(next(ciag))
# print(next(ciag))
# print(next(ciag))
# print(next(ciag))
# print(next(ciag))
# print(next(ciag))
