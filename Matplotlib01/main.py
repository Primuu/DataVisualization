import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt


# PROSTY WYKRES LINIOWY
# plt.plot([1, 2, 3, 4])
# plt.ylabel('liczby')
# plt.show()



# STYLE WYKRESOW
# # Przekazujemy dwa wektory wartosci, najpierw dla
# # wektora x, następnie dla wektora y. Dodatkowo mamy
# # tutaj przekazany parametr w postaci stringa, ktory
# # okresla styl wykresu
# # Pelna lista: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
# # tutaj określamy listę parametrow w postaci:
# # [xmin, xmax, ymin, ymax]
# plt.axis([0, 6, 0, 20])
# plt.show()

# Mozna tez ustawic rozne kolory dla poszczegolnych
# elementow nakladajac na siebie dwa wykresy
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
# plt.axis([0, 6, 0, 20])
# plt.show()



# Bazowy wektor wartosci
# t = np.arange(0., 5., 0.2)
# # Za pomoca pojedynczego wywolania funkcji plot()
# # mozna wygenerowac wiele wykresow na "jednym plotnie"
# # (ang. canvas). Kazdorazowo podajac niezbedne wartosci:
# # wartosci dla osi x, wartosci dla osi ym styl wykresu,...
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()




# Wykresy moga byc tez dodawane do "plotna" definicja
# po definicji, zamiast w pojedynczym wywolaniu plot().
# Tutaj zostal uzyty parametr label, ktory okresla
# etykiete danego wykresu w legendzie

# x = np.linspace(0, 2, 100)
# plt.plot(x, x, label="liniowa")
# plt.plot(x, x**2, label="kwadratowa")
# plt.plot(x, x**3, label="szescienna")
# # etykiety osi
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
# # tytul wykresu
# plt.title("Prosty wykres")
# # legenda
# plt.legend()
# plt.show()



# WYKRES SINUS
# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
# plt.plot(x, s, label="sin(x)")
# # etykieta osi
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# # tytuł wykresu
# plt.title('Wykres sin(x)')
# # legenda
# plt.legend()
# plt.show()



# Dane w postaci słownika (równie dobrze może to być
# Pandas DataFrame)
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# # Aby w ten sposób przekazać parametry wykresu, należy
# # dodać nizbędny parametr data, który zawiera dane
# # dostępne poprzez etykiety. Oznacza to, że 'a' jest
# # równoważne data['a'] itd. Parametr to skrót od color,
# # tutaj przekazywany w formie wektora wartości kolorów
# # dla każdej kolejnej wartości wykresu. Parametr s to
# # scale - określa rozmiar, w tym przypadku punkt
# # dla każdej każdej kolejnej wartości wektora wykresu.
# # Podsumowując: dla pierwszego punktu wykresu będą
# # brane poniższe wartości:
# print(f"a={data['a'][0]}, b={data['b'][0]}, c={data['c'][0]}, d={data['d'][0]}")
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('warotsc a')
# plt.ylabel('warotsc b')
# plt.show()



# ---PODWYKRESY---
# Podwykresy pozwalają na umieszczanie na jednym
# płótnie wielu wykresów zorganizowanych w formie gridu.
# Podajemy wymiary gridu, czyli liczbę wierszy oraz
# liczbę kolumn. Służy do tego funkcja 'subplot',
# która przyjmuje 3 argumenty(nrows, ncols, index).
# Odpowiednio jest to:
# ilość wierszy gridu
# ilość kolumn gridu
# indeks definiowanego własnie wykresu ( indeksy
# rozpoczynają się od 1 i kończą na nrows*cols)
# x1 = np.arange(0.0, 2.0, 0.02)
# x2 = np.arange(0.0, 2.0, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
# # mamy tu do czynienia z gridem 2x1 (2 wiersze, 1 ko-
# # lumna) i definiujemy wykres o indeksie 1
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1, '-')
# plt.title('Dwa podwykresy')
# plt.ylabel('sin(x)')
# # mamy tu do czynienia z gridem 2x1 (2 wiersze, 1 ko-
# # lumna) i definiujemy wykres o indeksie 2
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.show()



# 3 PODWYKRESY
# x1 = np.arange(0.0, 2.0, 0.02)
# x2 = np.arange(0.0, 2.0, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
# # mamy tu do czynienia z gridem 3x2 (3 wiersze, 2 ko-
# # lumna) i definiujemy wykres o indeksie 1
# plt.subplot(3, 2, 1)
# plt.plot(x1, y1, '-')
# plt.title('Trzy podwykresy')
# plt.ylabel('sin(x)')
# # Mozemy rowniez pominac przecinki, tu wykres
# # o indeksie 4, wiec pominelismy 2 oraz 3
# plt.subplot(324)
# plt.plot(x2, y2, 'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.subplot(325)
# plt.plot(x2, y2, 'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.show()



# PROSTY PRZYKŁAD WYKRESU SŁUPKOWEGO
# etykiety = ['Kobiety', 'Mezczyzni']
# wartosci = [345, 435]
# rozmiar_wykresu = plt.figure(figsize=(6, 10))
# plt.bar(etykiety, wartosci)
# # mozna zmienic np. kierunek tekstu etykiet slupkow
# plt.xticks(rotation=45)
# plt.ylabel('Ilosc narodzin')
# plt.xlabel('Plec')
# plt.show()



# Popularnym typem wykresow dla zaprezentowania rozkladow
# prawdopodobienstwa sa histogramy
# "bins" oznacza ilość "koszy" czyli slupkow, do ktorych
# maja wpadac wartosci z wektora x
# facecolor - kolory slupkow
# alpha - stopien przezroczystosci wykresu
# density - czy suma ilosci zostanie znormalizowana
# do rozkladu prawdopodobienstwa ( czeli przedzial [0, 1])
# x = np.random.randn(10000)
# plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
# plt.xlabel('Wartosci')
# plt.ylabel('Prawdopodobienstwo')
# plt.title('Histogram')
# # wyswietlenie siatki
# plt.grid()
# plt.show()




# WYKRESY KOLOWE
# Pierwsza wersja wykresu
# zawodnicy = ['Messi', 'Suarez', 'Debele', 'Coutinho']
# bramki = [48, 25, 13, 11]
# wedges, texts, autotexts = plt.pie(bramki, labels=zawodnicy,
#                                    autopct=lambda pct:
# "{:.1f}%".format(pct), textprops=dict(color='black'))
# plt.setp(autotexts, size=14, weight='bold')
# plt.title('Pierwsza wersja wykresu')
# plt.legend(title='Zawodnicy')
# plt.show()

# Druga wersja wykresu
# zawodnicy = ['Messi', 'Suarez', 'Debele', 'Coutinho']
# bramki = [48, 25, 13, 11]
# def prepare_label (pct, br):
#     absolute = int(np.ceil(pct / 100. * np.sum(br)))
#     return "{:.1f}% \n({}/{})".format(pct, absolute, sum(bramki))
#
#
# wedges, texts, autotexts = plt.pie(bramki, labels=zawodnicy,
#                                    autopct=lambda pct:
# prepare_label(pct, bramki), textprops=dict(color='black'),
# radius=1.2, labeldistance=1.02, startangle=70)
# plt.setp(autotexts, size=14, weight='bold')
# plt.title('Druga wersja wykresu')
# plt.legend(title='Zawodnicy', loc='lower left',
#            bbox_to_anchor=(-0.2, -0.1))
# plt.show()

# HOMEWORK 06.10

# 1

# x = np.arange(1, 21, 1)
# plt.plot(x, (1 / x), label="f(x)=1/x")
# plt.axis([0, 20, 0, 1])
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title("Wykres funkcji f(x) = 1/x dla x[1,20]")
# plt.legend()
# plt.show()

# 2

# x = np.arange(1, 21, 1)
# plt.plot(x, (1 / x), 'g>:', label="f(x)=1/x")
# plt.axis([0, 20, 0, 1])
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title("Wykres funkcji f(x) = 1/x dla x[1,20]")
# plt.legend()
# plt.show()

# 3

# x = np.arange(0, 30, 0.1)
# s = np.sin(x)
# c = np.cos(x)
# plt.plot(x, s, 'r', label="sin(x)")
# plt.plot(x, c, 'g', label="cos(x)")
# plt.xlabel('x')
# plt.ylabel('sin(x) cos(x)')
# plt.title('Wykres sin(x), cos(x)')
# plt.legend(loc='upper right')
# plt.show()

# 4

# x = np.arange(0, 30, 0.1)
# s = np.sin(x)
# plt.plot(x, 2+s, label="sin(x)")
# plt.plot(x, -s, label="sin(x)")
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres sin(x), sin(x)')
# plt.legend(loc='center left')
# plt.show()

# 5

# data = pd.read_csv("iris.csv", sep=',', decimal='.')
# df = pd.DataFrame(data)
#
# # przygotowanie wektora kolorow
# colors = np.random.randint(0, 50, len(df.index))
# # przygotowanie wektora z rozmiarami 'kropek' (mnożenie *5 opcjonalne)
# scale = [np.abs(df['sepal_length'] - df['sepal_width']) * 5]
# plt.scatter('sepal_length', 'sepal_width', c=colors, s=scale, data=df)
# plt.xlabel('sepal_length')
# plt.ylabel('sepal_width')
# plt.show()

# 6

# zad6 = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(zad6, header=0)
#
# # 6.1
#
# plt.subplot(1, 3, 1)
# grouped = df.groupby('Plec').agg({'Liczba': ['sum']}).unstack()
# grouped.plot.bar(color=['r', 'g'])
# plt.title('Wykres 1')
# plt.ylabel('Ilosc narodzin')
# plt.xlabel('Plec')
#
# # 6.2
#
# # Jesli kazdy rok ma byc widoczny na wykresie:
# # df['Rok'] = df['Rok'].astype(str)
# plt.subplot(1, 3, 2)
# x = df['Rok'].unique()
# kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba': ['sum']}).values
# mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba': ['sum']}).values
# plt.plot(x, kobiety, 'pink', label="Dziewczynki")
# plt.plot(x, mezczyzni, 'yellow', label="Mezczyzni")
# plt.title('Wykres 2')
# plt.ylabel('Ilosc narodzin w danym roku')
# plt.xlabel('Rok')
#
# # 6.3
#
# # bez funkcji flatten matplotlib wyrzuca wyjatek,
# # ktory informuje nas, ze nie mozna przekazywac parametru
# # jako tablicy wielowymiarowej, a w takiej postaci w tym przypadku
# # zwracany jest wektor y, korzystamy wiec z flatten(),
# # poznanej przy okazji omawiania biblioteki numpy
# suma_dz_rok = df.groupby(['Rok']).agg({'Liczba': ['sum']}).values.flatten()
# # print(suma_dz_rok)
# # x = df['Rok'].unique()
#
# plt.subplot(1, 3, 3)
# plt.bar(x, suma_dz_rok)
# plt.title('Wykres 3')
# plt.ylabel('Laczna ilosc narodzin w danym roku')
# plt.xlabel('Rok')
#
# plt.show()

# 7

# df = pd.read_csv('zamowienia.csv', sep=';')
#
# # liczenie ilosci zamowien dla kazdego sprzedawcy
# grouped_df = df.groupby(['Sprzedawca']).agg({'idZamowienia': "nunique"})
# grouped_df = grouped_df.reset_index()
# sprzedawcy = grouped_df['Sprzedawca']
# zamowienia = grouped_df['idZamowienia']
# # Explode "odsuwa" fragment wykresu
# # Explode mozna zrobic na rozne sposoby
# # Najprosciej jest zrobic wektor (musi mieć rozmiar, jak wektor y)
#
# explode = (0, 0.3, 0, 0, 0, 0, 0.2, 0.1, 0)
# # Mozna tez posluzyc sie forem, dla kazdego x, a dopiero potem
# # okreslic, ktore fragmenty zostana wysuniete i  o ile
#
# # explode = [0.0 for n in range(len(sprzedawcy.index))]
# # explode[np.random.randint(0, len(sprzedawcy.index))] = 0.2
#
# wedges, texts, autotexts = plt.pie(zamowienia, labels=sprzedawcy, autopct=lambda pct:
#                                    "{:.1f}%".format(pct), shadow=True, explode=explode, textprops=dict(color="black"))
# plt.setp(autotexts, size=11, weight="bold")
# plt.title("Procentowy udzial kazdego sprzedawcy")
# plt.show()
#
# # liczenie sum utargow dla kazdego sprzedawcy
# policzone = df.groupby('Sprzedawca')['Utarg'].sum()
# # explode
# explode = [0.0 for n in range(len(policzone.index))]
# explode[np.random.randint(0, len(policzone.index))] = 0.2
# policzone.plot.pie(subplots=True, autopct='%.2f %%', fontsize=8, explode=explode, shadow=True)
# plt.title("Procentowy udzial kwot zamowien sprzedawcow")
# plt.show()
