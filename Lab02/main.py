from math import *
import sys as system



######## 04.03
#
# #1
#
# list_of_movies = ["Once Upon a Time in the West",
#                   "2001: A Space Odyssey",
#                   "The Godfather",
#                   "Seven Samurai",
#                   "Pulp Fiction",
#                   "The Godfather II",
#                   "The Good, the Bad and the Ugly"]
#
# list_of_movies.reverse()
#
# list_of_movies.insert(5, "Seppuku")
# list_of_movies.insert(5, "One Flew Over the Cuckoo's Nest")
# list_of_movies.insert(5, "Apocalypse Now")
#
# print(list_of_movies)
#
# #2
#
# movies_dictionary = {1:"Once Upon a Time in the West",
#                      2:"2001: A Space Odyssey",
#                      3:"The Godfather",
#                      4:"Seven Samurai",
#                      5:"Pulp Fiction",
#                      6:"The Godfather II",
#                      7:"The Good, the Bad and the Ugly",
#                      8:"Seppuku",
#                      9:"One Flew Over the Cuckoo's Nest",
#                      10:"Apocalypse Now"}
#
# print(movies_dictionary)
#
# #3
#
# subjects_dicitionary = {'CAD':'CAD komputerowe wspomaganie programowania',
#                         'PS':'Programowanie strukturalne',
#                         'PH':'Przedmiot humanizujacy',
#                         'JA':'Jezyk angielski',
#                         'WD':'Wizualizacja danych',
#                         'MD':'Matematyka dyskretna dla informatykow',
#                         'AM':'Analiza matematyczna dla informatykow'}
#
# print(len(subjects_dicitionary.values()))
#
# #4
#
# number = input("Podaj dowolna liczbe: ")
# exponentiation = pow(float(number), float(number))
# print(exponentiation)
#
# #5
#
# system.stdout.write("Podaj ciag znakow:")
# any_string = system.stdin.readline()
# system.stdout.write("Liczba a wystepuje %d razy" % (any_string.count('a')))
#
# #6
#
# a = input('Podaj pierwsza liczbe: ')
# b = input('Podaj druga liczbe: ')
# c = input('Podaj trzecia liczbe: ')
#
# a = int(a)
# b = int(b)
# c = int(c)
#
# if (a % 2 == 0)  & (b > c):
#     print("Warunek spelniony")
# else:
#     print("Warunek niespelniony")
#
# #7      PROBLEM Z ZADANIEM
#
# numbers_list = [5, 6, 7.123, 4, 1.3, 3.14, 21.37, 1337, 71830]
#
# for number in numbers_list:
#     sum = float(number + (number - 1))
#     print(sum)
#     sum = 0
#
# #8
#
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
#
# #9
#
# one_to_six = [1, 2, 3, 4, 5, 6]
#
# for x in one_to_six:
#     if x == 1:
#         print('OOOOOO')
#     elif (x > 1) & (x < 6):
#         print('O    O')
#     else:
#         print('OOOOOO')
#
# #10
#
# number = input("Podaj liczbe: ")
#
# error = 0
# end = int(len(number) - 1)
# start = 0
# a = 0
#
# while start <= end:
#     if (number[start] >= '0') & (number[start] <= '9'):
#         start += 1
#     else:
#         error += 1
#         start += 1
#
# if error != 0:
#     print("To nie liczba")
# else:
#     print("W porzadku")
#
#



