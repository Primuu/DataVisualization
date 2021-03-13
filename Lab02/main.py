from math import *
import sys

# 04.03
# Examples of lists

# list1 = ['string', 5, 5.5, 5 + 5j]
# print(list1)
#
# # add at the end, the list remains a list
# list1.append('additional string')
# print(list1)
# list1.append([1, 2, 3])
# print(list1)
#
# # add at index
# list1.insert(0, 1)
# print(list1)
#
# # delete last / delete by index
# list1.pop()
# list1.pop(0)
# print(list1)
#
# # delete value
# list1.remove(5)
# print(list1)
#
# # delete value by index / delete list
# del list1[2]
# print(list1)
# # del list1
#
# # adding a sequence at the end
# list1.extend((2, 3, 4))
# print(list1)
#
# # reverse the order of the list
# list1.reverse()
# print(list1)
#
# # sort
# list2 = [5, 3, 7, 7.5, 1, 2, 0, -10]
# list2.sort()
# print(list2)

# Examples of dictionaries

# # key:value
# dictionary1 = {1 : 'first',
#                2 : 'second',
#                3:'third' }
# print(dictionary1)
#
# # adding key and value
# dictionary1[4] = 'fourth'
# print(dictionary1)
#
# # display by key
# print(dictionary1[4])
#
# # deleting by key (key and value)
# dictionary1.pop(1)
# print(dictionary1)
#
# # display keys
# print(dictionary1.keys())
#
# # display values
# print(dictionary1.values())
#
# # deleting by key (key and value) / deleting dictionary
# del dictionary1[2]
# print(dictionary1)
# # del dictionary1
# print(dictionary1)

# Data input examples

# text = input('Enter any text: ')
# print(text)  # the data entered is always string
# print(type(text))
#
# # integer input
# a = input('Enter integer: ')
# a = int(a)
# print(a)
#
# # float input
# b = input('Enter float: ')
# b = float(b)
# print(b)
#
# # complex
# c = complex(a, b)
# print(c)

# Data input (SYS) example

# system.stdout.write("Enter any text: ")  # don't end line with \n
# systext = system.stdin.readline()
# system.stdout.write(systext)

# Conditional statement example

# a = input("Enter integer: ")
# b = input("Enter another integer:")
# a = int(a)
# b = int(b)
# if a > b:
#     print(str(a) + " is greater than " + str(b))
# elif b > a:
#     print(str(b) + " is greater than " + str(a))
# else:
#     print("The numbers entered are equal")

# iterative instruction "for"

# for x in range(0, 6, 1):
#     print(x)
# else:
#     print("End")

# iterative instruction "while"

# z = 0
# while z != 10:
#     print(z)
#     z += 1
# else:
#     print("There was displayed " + str(z) + " numbers.")

# Error handling

# a = input("Enter number: ")
# b = input("Enter number: ")
#
# try:
#     c = int(a) / int(b)
#     print(int(c))
# except ZeroDivisionError:
#     print("division by zero - not allowed")

# HOMEWORK

# #1

# list_of_movies = ["Once Upon a Time in the West",
#                   "2001: A Space Odyssey",
#                   "The Godfather",
#                   "Seven Samurai",
#                   "Pulp Fiction",
#                   "The Godfather II",
#                   "The Good, the Bad and the Ugly"]
#
# print(list_of_movies)
# list_of_movies.reverse()
# print(list_of_movies)
#
# list_of_movies2 = ["Seppuku",
#                    "One Flew Over the Cuckoo's Nest",
#                    "Apocalypse Now"]
#
# index = 5
#
# for i in list_of_movies2:
#     list_of_movies.insert(index, i)
#     index += 1
#
# print(list_of_movies)

# #2

# movies_dictionary = {"Top 1" : "Once Upon a Time in the West",
#                      "Top 2" : "2001: A Space Odyssey",
#                      "Top 3" : "The Godfather",
#                      "Top 4" : "Seven Samurai",
#                      "Top 5" : "Pulp Fiction",
#                      "Top 6" : "The Godfather II",
#                      "Top 7" : "The Good, the Bad and the Ugly",
#                      "Top 8" : "Seppuku",
#                      "Top 9" : "One Flew Over the Cuckoo's Nest",
#                      "Top 10" : "Apocalypse Now"}
#
# print(movies_dictionary)

# #3

# subjects_dicitionary = {'CAD':'CAD komputerowe wspomaganie programowania',
#                         'PS':'Programowanie strukturalne',
#                         'PH':'Przedmiot humanizujacy',
#                         'JA':'Jezyk angielski',
#                         'WD':'Wizualizacja danych',
#                         'MD':'Matematyka dyskretna dla informatykow',
#                         'AM':'Analiza matematyczna dla informatykow'}
#
# print(len(subjects_dicitionary.values()))

# #4

# number = input("Podaj dowolna liczbe: ")
# exponentiation = pow(float(number), float(number))
# print(exponentiation)
#
# # lub
#
# number = input("Podaj dowolna liczbe: ")
# number = float(number)
# result = number ** number
# print(result)

# #5

# sys.stdout.write("Podaj ciag znakow:")
# any_string = sys.stdin.readline()
# sys.stdout.write("Liczba a wystepuje %d razy" % (any_string.count('a')))

# #6

# a = input('Podaj pierwsza liczbe: ')
# b = input('Podaj druga liczbe: ')
# c = input('Podaj trzecia liczbe: ')
#
# a = int(a)
# b = int(b)
# c = int(c)
#
# if (a % 2 == 0) & (b > c):
#     print("Warunek spelniony")
# else:
#     print("Warunek niespelniony")

# #7

# numbers_list = [5, 6, 7.123, 4, 1.3, 3.14, 21.37, 1337, 71830]
#
# for i in range(0, len(numbers_list), 1):
#     if i == 0:
#         print(numbers_list[i])
#     else:
#         sum_n = numbers_list[i] + numbers_list[i - 1]
#         print(sum_n)

# #8

# even_list = []
#
# i = 0
# while i < 10:
#     any_number = input('Podaj liczbe: ')
#     any_number = float(any_number)
#     if any_number % 2 == 0:
#         even_list.append(any_number)
#     i += 1
#
# print(even_list)

# #9

# one_to_six = [1, 2, 3, 4, 5, 6]
#
# for x in one_to_six:
#     for y in one_to_six:
#         if (x == 1) | (x == 6):
#             sys.stdout.write("O")
#         else:
#             if (y == 1) | (y == 6):
#                 sys.stdout.write("O")
#             else:
#                 sys.stdout.write(" ")
#     sys.stdout.write("\n")

# #10

# try:
#     number = input(u"Podaj liczbę:")
#     number = float(number)
#     print(number)
# except ValueError:
#     print(u"Wprowadzona wartość nie jest liczbą")

