import numpy as np

# tablica
a = np.arange(5)
b = np.array([0, 1])

print(a)
print(b)
# wypisanie typu zmiennej tablicy
print(type(a))
# wypisanie typu danych tablicy
print(a.dtype)

# inicjalizacja tablicy z konkretnym typem danych
c = np.arange(2, dtype='int64')
print("\n", c.dtype)

# zapisywanie kopii tablicy jako tablicy z innym typem
d = a.astype('float')
print("\n", d)
print(d.dtype)

# wypisanie rozmiaru tablicy
print("\n", a.shape)

# wypisanie ilości wymiarów tablicy
print("\n", a.ndim)

# tablica wielowymiarowa
# w tym przypadku parametrem przekazywanym do funkcji
# array jest obiekt, który zostanie skonwertowany na tablicę
# np. pythonowa lista
e = np.array([np.arange(2), np.arange(2)])

print("\n", e)
print(e.shape)
print(type(e))

# tworzenie macierzy wypełnionej zerami/jedynkami
zerowa = np.zeros((3, 3))
jedynkowa = np.ones((4, 4))

print("\n", zerowa)
print(zerowa.dtype)
print(jedynkowa)
print(jedynkowa.dtype)

# "pusta" macierz, wypełniona losowo
pusta = np.empty((4, 3))

print("\n", pusta)

# odwoływanie się do elementów
odwolanie1 = pusta[1, 2]
odwolanie2 = pusta[0, 0]

print("\n", odwolanie1)
print(odwolanie2)

# tworzenie macierzy uzupełnionej
uzupelniona = np.array([[4, 3], [2, 1]])

print("\n", uzupelniona)

# funkcja arange tworzy również ciągi liczb zmiennoprzecinkowych
liczby_arrange = np.arange(1, 2.1, 0.1)

print("\n", liczby_arrange)
# podobnie działa funkcja linspace, z tą różnicą, że dzieli przedział
liczby_linspace = np.linspace(1, 2, 5)

print("\n", liczby_linspace)

# tworzenie macierzy kolumna -> wiersz z numerami
f = np.indices((5, 3))

print("\n", f)

# wielowymiarowe macierze - funkcja mgrid
g, h = np.mgrid[0:5, 0:5]

print("\n", g)
print(h)

# macierze diagonalne
macierz_diag = np.diag([a for a in range(5)])

print("\n", macierz_diag)

# przesunięcie przekątnej o indeks
mac_diag_k = np.diag([a for a in range(3)], 1)
print("\n", mac_diag_k)

# numpy jest w stanie stworzyć tablicę jednowymiarową
# z dowolnego obiektu iterowalnego (iterable)
i = np.fromiter(range(5), dtype='int32')

print("\n", i)

# funkcja frombuffer, może tworzyć np. tablicę znaków
# funkcja ta, ma jednak wadę dla pythona 3.x, która powoduje
# że, trzeba jawnie określić, iż ciąg znaków przekazujemy
# jako ciąg bajtów (podanie litery 'b' przed wartością)
konstantynopol = b'konstantynopol'
kon = np.frombuffer(konstantynopol, dtype='S1')
kon_2 = np.frombuffer(konstantynopol, dtype='S2')

print("\n", kon)
print(kon_2)

# można to też zrobić inaczej
warszawa = 'Warszawa'
war_1 = np.array(list(warszawa))
war_2 = np.array(list(warszawa), dtype='S1')
war_3 = np.array(list(b'Warszawa'))
war_4 = np.fromiter(warszawa, dtype='S1')
war_5 = np.fromiter(warszawa, dtype='U1')

print("\n", war_1)
print(war_2)
print(war_3)
print(war_4)
print(war_5)

# możliwe jest dodawanie, odejmowanie,
# mnożenie i dzielenie w prosty sposób
jedynkowa_1 = np.ones((2, 2))
jedynkowa_2 = np.ones((2, 2))
jedynkowa_1 = jedynkowa_1 + jedynkowa_2

print("\n", jedynkowa_1)
print(jedynkowa_1 - jedynkowa_2)
print(jedynkowa_1 * jedynkowa_1)
print(jedynkowa_2 / jedynkowa_1)

# indeksowanie i cięcie tablic
# cięcie (slicing) tablicy numpy można wykonać za pomocą
# wartości z funkcji slice lub range
j = np.arange(10)
j_s = slice(2, 7, 2)
j_r = range(2, 7, 2)

print("\n", j)
print(j[j_s])
print(j[j_r])
print(j[2:7:2])
print(j[1:])
print(j[2:5])
# w podobny sposób postępuje się z tablicami wielowymiarowymi

# zmina ksztatu tablicy jednowymiarowej na macierz 5x5
k = np.arange(25)
mat_k = k.reshape((5, 5))

print("\n", mat_k)
print("\n", mat_k[1:])                 # od drugiego wiersza
print("\n", mat_k[:, 1])               # druga kolumna -> wektor
print("\n", mat_k[..., 1])             # to samo (ellipsis(...))
print("\n", mat_k[:, 1:2])             # druga kolumna jako ndarray
print("\n", mat_k[:, -1:])             # ostatnia kolumna
print("\n", mat_k[2:6, 1:3])           # 2 i 3 kolumna dla 3,4,5 wierszy
print("\n", mat_k[:, range(2, 6, 2)])  # 3 i 5 kolumna

# bardziej zaawansowane  i trudniejsze cięcia
# y - tablica zawierająca wierzchołki macierzy x
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])

print("\n", x)

rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]

print("\n", y)

# HOMEWORK

# 1

task_1 = np.arange(4, 81, 4)

print(task_1)

# 2

task_2 = np.arange(5, dtype='float')
task2_1 = task_2.astype('int32')

# 3 PROBLEM

def foo3 (n):
    tablica = np.zeros((n, n), dtype='int32')
    i = 0
    for x in range(n):
        for y in range(n):
            tablica[x][y] = 2 ** i
            i += 1
    return tablica


print("\n", foo3(3))

# 4

def foo4 (base1, number):
    return np.logspace(1, number, number, base=base1)


print(foo4(2, 4))

# 5

def foo5 (length):
    return np.diag(range(length, 0, -1), 2)


print("\n", foo5(5))

# 6

puzzle = np.array([['K', 'A', 'J', 'A', 'K'],
                   ['A', 'A', 'q', 'w', 'e'],
                   ['J', 'r', 'J', 't', 'y'],
                   ['A', 'u', 'i', 'A', 'o'],
                   ['K', 'p', 'a', 's', 'K']])

print(puzzle)

# 7 PROBLEM

def foo7 (n):
    array = np.diag([2 for _ in range(n)])
    for index in range(1, n):
        vec = [2 + (2 * index) for _ in range(n - index)]
        array += np.diag(vec, index)
        array += np.diag(vec, -index)
    return array


print(foo7(10))

# 8 PROBLEM

def foo8 (tab, kierunek = 'poziomo'):
    print(tab)
    if kierunek == 'poziomo':
        if tab.shape[0] % 2 != 0:
            print("Tablica posiada nieparzysta liczbe wierszy.")
            return
        p1 = tab[0: int(tab.shape[0]/2),: ]
        p2 = tab[int(tab.shape[0]/2):, :]
        print("czesc 1")
        print(p1)
        print("czesc 2")
        print(p2)
    elif kierunek == "pionow":
        if tab.shape[1] % 2 != 0:
            print("Tablica posiada nieparzysta liczbe kolumn.")
            return
        p1 = tab[:, 0:int(tab.shape[1] / 2)]
        p2 = tab[:, int(tab.shape[1] / 2):]
        print("czesc 1")
        print(p1)
        print("czesc 2")
        print(p2)


foo8(np.arange(36).reshape((6, 6)), kierunek='pionowo')
# 9

# arithmetic sequence with a difference of 5
task_9 = np.arange(0, 121, 5)
task_9 = task_9.reshape((5, 5))

print(task_9)




