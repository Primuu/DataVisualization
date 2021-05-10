import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

# # SZEREG CZASOWY DANYCH, radnom + data_range
# ts = pd.Series(np.random.randn(2300), index=pd.date_range('1/1/2015', periods=2300))
# print(ts)
#
# # Funkcja generująca sumę kolejnych elementów - wykres
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()
#
#
#
# # WYKRES KOLUMNOWY
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Pd', 'Europa'],
#         'Populacja': [11904265, 1246950324, 267695324, 37124245]}
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
# print(grupa)
#
# wykres = grupa.plot.bar()
# wykres.set_ylabel("Mld")
# wykres.set_xlabel("Kontynent")
# wykres.legend()
# plt.title("Populacja z podzialem na kontynenty")
# # zmiana kierunku tekstu etykiet słupkow
# plt.xticks(rotation=0)
# plt.savefig('wykres.png')
# plt.show()
#
# wczytanie danych z plikow i wyswietlenie zgrupowanych rzeczy
# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
# print(df)
# grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia': ['sum']})
# # wykres kolowy z wartosciami procentowymi sformatowanymi z dokladoscia do 2 miejsc po przecinku
# # figsize ustawia wielkosc wykresu w calach, domyslnie 6,4 i 4,8
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6), legend=(0, 0))
# plt.legend(loc="lower right")
# plt.title('Suma zamowienia dla przedawcy')
# plt.show()
#
# # wykres sredniej kroczacej
# ts = pd.Series(np.random.randn(2300), index=pd.date_range('1/1/2015', periods=2300))
# print(ts)
#
# ts = ts.cumsum()
# df = pd.DataFrame(ts)
# # dodanie nowej kolumny i wykorzystanie
# # funkcji rolling do stworzenia kolejnych wartosci
# # sredniej kroczacej
# df['MA'] = df.rolling(window=50).mean()
# df.plot()
# plt.show()


# HOMEWORK 29.04

# 1

task1 = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(task1, header=0)
print(df)

# df['Rok'] = df['Rok'].astype(str)
# group = df.groupby(['Rok']).agg({'Liczba': ['sum']})
# chart = group.plot()
# chart.set_ylabel("Liczba urodzonych dzieci")
# chart.set_xlabel("Rok")
# chart.legend()
# plt.title("Liczba urodzonych dzieci w danym roku")
# plt.show()


# 2

# group = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# chart = group.plot.bar()
# chart.set_ylabel(u"Liczba urodzeń")
# chart.set_xlabel(u"Płeć")
# chart.legend()
# plt.title(u"Liczba urodzonych chłopców i dziewczynek")
# plt.xticks(rotation=0)
# plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
# plt.show()

# 3

# df = df[(df['Rok'] >= 2013) & (df['Rok'] <= 2017)]
# # print(df)
# group = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# chart = group.plot.pie(subplots=True, autopct='%.2f %%',
#                        fontsize=20, figsize=(6, 6), legend=(0, 0))
# plt.legend(loc="lower right")
# plt.title(u"Stosunek urodzeń chłopców i dziewczynek w ostatnich 5 latach")
# plt.show()

# 4

# dfz = pd.read_csv('zamowienia.csv', header=0, sep=";",
#                   decimal='.')
# # print(dfz)
# group = dfz.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})
# chart = group.plot.bar(figsize=(8, 8))
# chart.set_ylabel(u"Ilość złożonych zamówień")
# chart.set_xlabel(u"Sprzedawca")
# chart.legend()
# plt.title(u"Ilość złożonych zamówień przez poszczególnych sprzedawców")
# plt.xticks(rotation=0)
# plt.show()
















