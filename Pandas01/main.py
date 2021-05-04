import pandas as pd
import numpy as np
import xlrd
import openpyxl







# Series
a = pd.Series([1, 3, 5, np.nan, 6, 8])
print(a)
a = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek',
                                      'Wiesiek', 'Kot'])
print(a)







# DataFrame
# DataFrame utworzony na podstawie słownika
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}
df1 = pd.DataFrame(data)
print(df1)

# DataFrame przechowuje typ dla każdej kolumny co możemy
# sprawdzić wpisując
print(df1.dtypes)

# Łatwo tworzy się serię danych - czyli próbki dla
# kolejnych dat, pomiarów czasu
# ('20210324' - rok, miesiac, dzień|periods=5 - 5 kolejnych)
daty = pd.date_range('20210324', periods=5)
print(daty)
df2 = pd.DataFrame(np.random.randn(5, 4), index=daty,
                  columns=list('ABCD'))
print(df2)


# Biblioteka Pandas umożliwia tworzenie DataFrameów
# z zewnętrznych źródeł danych
# CSV, odczyt i zapis
df3 = pd.read_csv('dane.csv', header=0, sep=";",
                  decimal=',')
print(df3)
df3.to_csv('plik.csv', index=False)

# Excel - wymagane są biblioteki xlrd oraz openpyxl
# przed importem trzeba je zainstalować
# xlsx = pd.ExcelFile('dane.xlsx')
# df4 = pd.read_excel(xlsx, header=0)
# print(df4)
# df4.to_excel('wyniki.xlsx', sheet_name="arkusz pierwszy")







# POBIERANIE DANYCH ZE STRUKTUR
# (a i df1 z początku)
# Pojedynczy element serii, odnosimy się do nazwy indeksu
print("\n", a['Wiesiek'])

# Możemy dostać się do wartości serii jak do pola klasy
print(a.Wiesiek)

# Pojedynczy element ramki danych, tak jak przy cięciu, tablic,
# (z tą różnicą, że tu opiera się to o indeksy)
print(df1[0:1])
print("")
# Kolumna - po etykiecie
print(df1['Populacja'])

# Pobieranie pojedynczej wartości (po indeksie wiersza i kolumny)
print(df1.iloc[[0][0]])
# Pobieranie wartości (po indeksie wiersza i etykiecie kolumny)
print(df1.loc[[0], ["Kraj"]])
# Prawie to samo, co:
print(df1.at[0, 'Kraj'])

# Podobnie jak w przypadku serii, można odwoływać się do kolumn
# jak do pól klasy. Dodatkowo print jest wywoływany jak w pętli
# dla każdego elementu danej kolumny
print('kraj:' + df1.Kraj)


# Pandas posiada również funkcje pozwalające na losowe
# pobieranie elementów lub w odniesieniu do procentowej
# wielkości całego zbioru

# jeden losowy element
print(df1.sample())
# n losowych elementów
n = 3
print(df1.sample(n))
# ilość elementów procentowo, uwaga na zaokrąglenie
print("\n", df1.sample(frac=0.5), "\n")

# jeżeli potrzeba więcej próbek, niż jest w zbiorze
# (i dopuszczamy duplikaty) => replace - losuje z powtórzeniami
print(df1.sample(10, replace=True), "\n")

# zamiast wyświetlać całą kolekcję, możemy wyświetlać
# określoną ilość elementów od początku kolekcji lub od jej końca
print(df1.head(), "\n")
print(df1.head(2), "\n")
print(df1.tail(1), "\n")


# Pandas jest w stanie wyświetlić statystykę dla wartości,
# które dana kolekcja zawiera, o ile są jakieś kolumny
# z danymi numerycznymi
print(df1.describe())
# Transpozycja to zmienna T kolekcji, podobnie jak w numpy
print(df1.T)







# FILTROWANIE, GRUPOWANIE I AGREGOWANIE DANYCH
# (a i df1 z początku)
# Wyświetlanie danych z serii gdzie wartość > 1
print(a[(a > 9)])
# Nieco inny efekt można osiągnąć funkcją "where",
# która zwaraca kolekcję w oryginalnej wielkości
print(a.where(a > 9))
# Można podać wartość, która zostanie podstawiona pod NaN
print(a.where(a > 9, 'za duże'), "\n")
# Jeszcze inna własność "where" pozwala na modyfikowanie
# oryginalnego zbioru (domyślnie zwracana jest kopia)
seria = a.copy()
seria.where(seria > 10, 'za duże', inplace=True)
print("########")
print(seria)
print(a)

# Wyświetlanie danych z serii gdzie wartość nie jest wieksza od 10
print(a[~(a > 10)])
# Warunki można łączyć
print(a[(a < 13) & (a > 8)])


# Warunki dla pobierania DataFrame
print(df1[df1['Populacja'] > 1200000000])
print(df1[((df1.Populacja > 1000000) & (df1.index.isin([0, 2])))])
# Inny przykład z listą dopuszczalnych wartości oraz isin
# zwracająca wartości bool
search = ['Belgia', 'Brasilia']
print("\n", df1.isin(search))



# Zmiana, usuwanie i dodawanie danych
# W przypadku serii można dodać/zmienić wartość poprzez
# odwołanie się do elementu serii przez klucz(indes)
a['Wiesiek'] = 15
print("\n", a.Wiesiek)
a['Alan'] = 16
print("\n", a)

# Podobna operacja dla DataFrame ma nieco inny efekt - wartość
# ustawiona dla wsszystkich kolumn
df1.loc[3] = 'dodane'
print(df1)
# Można dodać wiersz w postaci listy
df1.loc[4] = ['Polska', 'Warszawa', 38675467]
print(df1)

# Usuwanie danych można wykonać przez funkcję "drop", ale
# należy pamiętać, że operacja nie wykonuje się in-place więc
# zwracana jest kopia DataFrame z usuniętymi wartościami
nowe_df = df1.drop([3])
print("\n\n", nowe_df)
# Więc jeżeli chcemy zmienić pierwotny zbiór, dodajemy parametr
# inplace=True
df1.drop([3], inplace=True)
print("\n\n", df1)

# Można usuwać również całe kolumny po nazwie indeksu
nowe_df.drop('Kraj', axis=1, inplace=True)
print("\n\n", nowe_df)

# Można dodać kolumny zamiast wierszy
df1['Kontynent'] = ['Europa', 'Azja',
                    'Ameryka Południowa', 'Europa']
print("\n\n", df1)

# Pandas ma własne funkcje:
# sortowania danych
print("\n\n", df1.sort_values(by='Kraj'))

# grupwoania
grouped = df1.groupby(['Kontynent'])
print("\n\n", grouped.get_group('Europa'))
# Można (podobnie jak w Excelu lub SQLu uruchamiać funkcje
# agregujące na danej kolumnie
print(df1.groupby(['Kontynent']).agg({'Populacja':['sum']}))

# Podobny mechanizm to sumy częściowe i tablice przestawene
# znane z Excela, które w Pandas rónież mają swoje odpowiedniki
print("_____sumy częściowe_____")
tabela = pd.pivot_table(df1, values=['Populacja'],
                        index=['Kontynent'], columns=['Kraj'],
                        aggfunc=np.sum, margins=True)
print(tabela.stack('Kraj'))



# HOMEWORK 22.04

# 1

zad1 = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(zad1, header=0)
print(df)


# 2
# 2.1
print(df[(df['Liczba'] < 1000)])
print('\n')
# 2.2
print(df[(df['Imie'] == "ADAM")])
print('\n')
# 2.3
print(sum(df.Liczba))
print('\n')
# 2.4
print(sum(df.Liczba[((df['Rok'] >= 2005) & (df['Rok'] <= 2010))]))
# 2.5
print(sum(df.Liczba[((df['Rok'] == 2000) & (df['Plec'] == 'M'))]))
# 2.6
for x in range(2000, 2018, 1):
    print("Rok ", x)
    print(df['Imie'][df['Liczba'] == max(df['Liczba'][((df['Rok'] == x) & (df['Plec'] == 'K'))])])
    print(df['Imie'][df['Liczba'] == max(df['Liczba'][((df['Rok'] == x) & (df['Plec'] == 'M'))])])
print('\n')
# 2.7 PROBLEM
# print(df['Imie'][df['sum'] == max(df.groupby(['Imie']).agg({'Liczba': ['sum']})[(df['Plec'] == 'K')])])
# print(df['Imie'][df['sum'] == max(df.groupby(['Imie']).agg({'Liczba': ['sum']})[(df['Plec'] == 'M')])])
print('\n')

# 3
dfz = pd.read_csv('zamowienia.csv', header=0, sep=";",
                  decimal='.')
# 3.1
print(pd.unique(dfz.Sprzedawca), '\n')
# 3.2
utarg_malejaca = dfz.Utarg.sort_values(ascending=False)
print(utarg_malejaca[0:5], '\n')
# 3.3
print(pd.value_counts(dfz.Sprzedawca), '\n')
# 3.4
print(dfz.groupby(['Kraj']).agg({'idZamowienia': ['count']}), '\n')
# 3.5 PROBLEM

# 3.6
dfz['Data zamowienia'] = pd.to_datetime(dfz['Data zamowienia'])
start_date = pd.to_datetime('1/1/2004')
end_date = pd.to_datetime('12/31/2004')
print(np.average(dfz.Utarg[(dfz['Data zamowienia'] >= start_date) & (dfz['Data zamowienia'] <= end_date)]), '\n')
# 3.7
dfz['Data zamowienia'] = pd.to_datetime(dfz['Data zamowienia'])
start_date2004 = pd.to_datetime('1/1/2004')
end_date2004 = pd.to_datetime('12/31/2004')
start_date2005 = pd.to_datetime('1/1/2005')
end_date2005 = pd.to_datetime('12/31/2005')
dfz2004 = dfz.loc[(dfz['Data zamowienia'] >= start_date2004) & (dfz['Data zamowienia'] <= end_date2004)]
dfz2005 = dfz.loc[(dfz['Data zamowienia'] >= start_date2005) & (dfz['Data zamowienia'] <= end_date2005)]
print(dfz2004)
dfz2004.to_csv('zamowienia_2004.csv', sep=';')
print(dfz2005)
dfz2005.to_csv('zamowienia_2005.csv', sep=';')












