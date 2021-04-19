import numpy as np

# 1. OPERACJE NA TABLICACH
# 1.1

# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# print(a)
# print(b, "\n")
#
# c = a - b
# print(c)
# print(b ** 2)
# a += b
# print(a)
# a -= b
# print(a)

# 1.2

# d = np.arange(12).reshape(3, 4)
# print(d)
# # suma całej macierzy
# print(d.sum())
# # suma każdej z kolumn
# print(d.sum(axis=0))
# # minimum każdego rzędu
# print(d.min(axis=1))
# # skumulowana suma dla rzędu
# print(d.cumsum(axis=1))

# 1.3

# e = np.arange(3)
# f = np.arange(3)
# # iloczyn macierzy
# print(e.dot(f))
# print(np.dot(e, f))

# 1.4

# g = np.ones(3, dtype='int32')
# h = np.linspace(0, np.pi, 3)
# i = g + h
# print(i)
# j = np.exp(i * 1j)
# print(j)

# 2. FUNKCJE UNIWERSALNE
# 2.1

# k = np.arange(3)
# print(k)
# print(np.exp(k))
# print(np.sqrt(k))
# l = np.array([2., -1., 4.])
# print(np.add(k, l))

# 3. ITERACJA TABLIC
# 3.1

# Tablice wielowymiarowe iterujemy w oniesieniu do pierwszej osi
# m = np.arange(6).reshape(3, 2)
# print(m)
# for x in m:
#     print(x)
#     print("")

# 3.2

# n = np.arange(6).reshape(3, 2)
# print(n)
# for x in n.flat:
#     print(x)
#     print("")

# 4. PRZEKSZTAŁCENIA
# 4.1

# o = np.arange(6)
# print(o)
# print(o.shape)
# print("")
# # u = np.array([np.arange(3), np.arange(3), np.arange(3)])
# # print(u)
# # print(u.shape)
#
# # Przekształcenie macierzy o na macierz 2x3
# p = o.reshape(2, 3)
# print(p)
# print(p.shape)
# print("")
#
# # Przekształcenie macierzy o na macierz 3x2
# r = o.reshape(3, 2)
# print(r)
# print(r.shape)
# print("")
#
# # Spłaszczenie macierzy
#
# s = r.ravel()
# print(s)
# print(s.shape)
# print("")
#
# # Transpozycja macierzy
#
# t = p.T
# print(t)
# print(t.shape)


# HOMEWORK 15.04
# 1

a1 = np.arange(3)
a2 = np.arange(3, 6)
print(a1 * a2)

# 2

b1 = np.arange(9).reshape(3, 3)
b2 = np.arange(9, 25).reshape(4, 4)
# minimum każdego rzędu
print(b1.min(axis=1))
print(b2.min(axis=1))
# minimum każdej kolumny
print(b1.min(axis=0))
print(b2.min(axis=0))

# 3

print(a1.dot(a2))

# 4

c1 = np.ones(3, dtype='int32')
c2 = np.linspace(0, np.pi, 3)
print(c1 * c2)

# 5

d5 = np.arange(4, 10).reshape(2, 3)
zad5 = np.sin(d5)
print(zad5)


# 6

d6 = np.arange(9, 15).reshape(2, 3)
zad6 = np.cos(d6)
print(zad6)

# 7

e = zad5 + zad6
print(e)

# 8

zad8 = np.arange(9).reshape(3, 3)
for x in zad8:
    print(x)

# 9

zad9 = np.arange(9, 18).reshape(3, 3)
for x in zad9.flat:
    print(x)

# 10

zad10 = np.arange(81)
print(zad10)
# Reshape :
a = zad10.reshape(9, 9)
# W pętli -> flat, spłaszczenie do 1 kolumny:
for x in zad10.flat:
    print(x)
# Ravel
zad10 = zad10.ravel()
print(zad10)
# Transpozycja
zad10 = zad10.reshape(9, 9)
zad10 = zad10.T
print(zad10)

# 11

zad11 = np.arange(12).reshape(3, 4)
print(zad11)
zad11 = zad11.ravel()
print(zad11)
zad11 = zad11.reshape(4, 3)
print(zad11)
zad11 = zad11.ravel()
print(zad11)
zad11 = zad11.reshape(2, 6)
zad11 = zad11.ravel()
print(zad11)




