import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data
from matplotlib.colors import LightSource

# WYKRESY 3D

# Wykres liniowy

# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# t = np.linspace(0, 2 * np.pi, 100)
# z = t
# x = np.sin(t) * np.cos(t)
# y = np.tan(t)
# ax.plot(x, y, z, label='Wykres 1')
# ax.legend()
# plt.show()

# Wykres punktowy

# # Stały seed - za każdym razem wygląda tak samo
# np.random.seed(19680801)
#
#
# def randrange(n, vmin, vmax):
#     """Funkcja wspomagajaca moze tworzyc macierz
#     losowych liczb o ksztalcie (n, )"""
#     return (vmax - vmin) * np.random.rand(n) + vmin
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# n = 100
#
# # Dla kazdego zbioru styli i zakresow wygeneruje n losowych
# # punktow. Zdefiniowane przez x z [23, 32], y z [0, 100],
# # z z [zlow, zhigh].
# for c, m, zlow, zhigh in [('r', 'o', -50, -25),
#                           ('b', '^', -30, -5)]:
#     xs = randrange(n, 23, 32)
#     ys = randrange(n, 0, 100)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)
#
# ax.set_xlabel('X label')
# ax.set_ylabel('Y label')
# ax.set_zlabel('Z label')
# plt.show()

# Wykres powierzchniowy

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# # generuj dane
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# # rysuj powierzchnie
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# # dodanie paska kolorow
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.show()

# PRZYKLAD WYKRESU ZACIENIONEGO I NIE ZACIENIONEGO

# # konfiguracja wielkosci wykresu:
# # figsize okresla wielkosc wykresu w calach
# fig = plt.figure(figsize=(8, 3))
# ax1 = fig.add_subplot(121, projection='3d')
# ax2 = fig.add_subplot(122, projection='3d')
# # dane
# _x = np.arange(4)
# _y = np.arange(5)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y = _xx.ravel(), _yy.ravel()
# top = x + y
# bottom = np.zeros_like(top)
# width = depth = 1
# ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
# ax1.set_title('Wykres zacieniony')
# ax2.bar3d(x, y, bottom, width, depth, top, shade=False)
# ax2.set_title('Wykres nie zacieniony')
# plt.show()





# WIELE WYKRESOW W JEDNYM WYWOLANIU

# # szerokosc 2 razy wieksza niz wysokosc
# fig = plt.figure(figsize=plt.figaspect(0.5))
# # Pierwszy wykres:
# # osie dla pierwszego wykresu
# ax = fig.add_subplot(1, 2, 1, projection='3d')
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# surf = ax.plot_surface(X, Y, Z,
#                        cmap=cm.coolwarm, linewidth=1,
#                        antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf, shrink=0.5, aspect=10)
#
# # Drugi wykres:
# # osie dla drugiego wykresu:
# ax = fig.add_subplot(1, 2, 2, projection='3d')
# X, Y, Z = get_test_data()
# ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
# plt.show()





# WIELE TYPOW WYKRESOW W JEDNEJ PRZESTRZENI

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# x = np.linspace(0, 1, 100)
# y = np.sin(x * 2 * np.pi) / 2 + 0.5
# ax.plot(x, y, zs=0, zdir='z', label='curve in (x,y)')
# colors = ('r', 'g', 'b', 'k')
# np.random.seed(19680801)
# x = np.random.sample(20 * len(colors))
# y = np.random.sample(20 * len(colors))
# c_list = []
# for c in colors:
#     c_list.extend([c] * 20)
#
# # przez uzycie zdir='y', wartosc y dla tych punktow jest
# # rowne zs czyli 0. Punkty (x,y) sa nakladane na osiach x i z
# ax.scatter(x, y, zs=0, zdir='y', c=c_list,
#            label='points in (x,z)')
# # Limity dla legendy
# ax.legend()
# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
# ax.set_zlim(0, 1)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# # Ustawienie kata nachylenia przy generowaniu wykresu
# # oś y=0
# ax.view_init(elev=20., azim=-35)
# plt.show()





# HOMEWORK 13.05

# 1

# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# t = np.linspace(0, 2 * np.pi, 100)
# z = t
# x = np.sin(t)
# y = 2 * np.cos(t)
# ax.plot(x, y, z, label='Zadanie 1')
# ax.legend()
# plt.show()

# 2

# # Stały seed - za każdym razem wygląda tak samo
# np.random.seed(19680801)
#
#
# def randrange(n, vmin, vmax):
#     """Funkcja wspomagajaca moze tworzyc macierz
#     losowych liczb o ksztalcie (n, )"""
#     return (vmax - vmin) * np.random.rand(n) + vmin
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# n = 100
#
# # Dla kazdego zbioru styli i zakresow wygeneruje n losowych
# # punktow. Zdefiniowane przez x z [23, 32], y z [0, 100],
# # z z [zlow, zhigh].
# for c, m, zlow, zhigh in [('red', 's', -10, 0),
#                           ('green', 'P', -20, -10),
#                           ('black', '+', -30, -20),
#                           ('blue', '.', -40, -30),
#                           ('yellow', '4', -50, -40)]:
#     xs = randrange(n, 0, 40)
#     ys = randrange(n, 0, 40)
#     zs = randrange(n, zlow, zhigh)
#     ax.scatter(xs, ys, zs, c=c, marker=m)
#
# ax.set_xlabel('X label')
# ax.set_ylabel('Y label')
# ax.set_zlabel('Z label')
# plt.show()

# 3

# fig = plt.figure(figsize=(16, 9))
# # generuj dane
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# # rysuj powierzchnie 1
# ax = fig.add_subplot(2, 3, 1, projection='3d')
# surf = ax.plot_surface(X, Y, Z, cmap=cm.hot,
#                        linewidth=1, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf, shrink=0.5, aspect=10, orientation='vertical',
#              pad=0.1)
# # rysuj powierzchnie 2
# ax = fig.add_subplot(2, 3, 2, projection='3d')
# surf1 = ax.plot_surface(X, Y, Z, cmap=cm.Pastel1,
#                         linewidth=1, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf1, shrink=0.5, aspect=10, orientation='vertical',
#              pad=0.1)
# # rysuj powierzchnie 3
# ax = fig.add_subplot(2, 3, 3, projection='3d')
# surf2 = ax.plot_surface(X, Y, Z, cmap=cm.ocean,
#                         linewidth=1, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf2, shrink=0.5, aspect=10, orientation='vertical',
#              pad=0.1)
# # rysuj powierzchnie 4
# ax = fig.add_subplot(2, 3, 4, projection='3d')
# surf3 = ax.plot_surface(X, Y, Z, cmap=cm.Spectral,
#                         linewidth=1, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf3, shrink=0.5, aspect=10, orientation='vertical',
#              pad=0.1)
# # rysuj powierzchnie 5
# ax = fig.add_subplot(2, 3, 5, projection='3d')
# surf4 = ax.plot_surface(X, Y, Z, cmap=cm.PiYG,
#                         linewidth=1, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf4, shrink=0.5, aspect=10, orientation='vertical',
#              pad=0.1)
#
#
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#
# # zapis PNG
# plt.savefig('zad3.png')
# plt.show()

# 4 MALA ROZNORODNOSC

# # konfiguracja wielkosci wykresu:
# # figsize okresla wielkosc wykresu w calach
# fig = plt.figure(figsize=(11, 4))
# ax1 = fig.add_subplot(151, projection='3d')
# ax2 = fig.add_subplot(152, projection='3d')
# ax3 = fig.add_subplot(153, projection='3d')
# ax4 = fig.add_subplot(154, projection='3d')
# ax5 = fig.add_subplot(155, projection='3d')
# # dane
# _x = np.arange(4)
# _y = np.arange(5)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y = _xx.ravel(), _yy.ravel()
# top = x + y
# bottom = np.zeros_like(top)
# width = depth = 1
# colors = ['r', 'g', 'b', 'm', 'c', 'y']
# ls = LightSource(azdeg=225.0, altdeg=45.0)
# ax1.bar3d(x, y, bottom, width, depth, top, color='red', shade=True)
# ax1.set_title('Wykres 1')
# ax2.bar3d(x, y, bottom, width, depth, top, color='green', shade=False)
# ax2.set_title('Wykres 2')
# ax3.bar3d(x, y, bottom, width, depth, top, color='orange', shade=True, lightsource=ls)
# ax3.set_title('Wykres 3')
# ax4.bar3d(x, y, bottom, width, depth, top, shade=False)
# ax4.set_title('Wykres 4')
# for i in range(6):
#     ax5.bar3d(x, y, bottom, width, depth, top, color=colors[i], alpha=0.1)
# ax5.set_title('Wykres 5')
# plt.show()

# 5

# fig = plt.figure(figsize=(16, 9))
# ax1 = fig.add_subplot(121, projection='3d')
# # generuj dane wykresu 1
# X1 = np.arange(-5, 5, 0.25)
# Y1 = np.arange(-5, 5, 0.25)
# X1, Y1 = np.meshgrid(X1, Y1)
# R1 = np.sqrt(X1**2 + Y1**2)
# Z1 = np.sin(R1)
# # rysuj powierzchnie wykresu 1
# surface1 = ax1.plot_surface(X1, Y1, Z1, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# ax1.set_zlim(-1.01, 1.01)
# ax1.zaxis.set_major_locator(LinearLocator(10))
# ax1.zaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# fig.colorbar(surface1, shrink=0.5, aspect=5)
# ax1.set_title('Wykres pierwotny')
#
# ax2 = fig.add_subplot(122, projection='3d')
# # generuj dane wykresu 2
# X2 = np.arange(-5, 5, 0.1)
# Y2 = np.arange(-5, 5, 0.1)
# X2, Y2 = np.meshgrid(X2, Y2)
# R2 = np.sqrt(X2**2 + Y2**2)
# Z2 = np.sin(R2)
# # rysuj powierzchnie wykresu 2
# surface2 = ax2.plot_surface(X2, Y2, Z2, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=True)
# ax1.set_zlim(-1.01, 1.01)
# ax1.zaxis.set_major_locator(LinearLocator(10))
# ax1.zaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# fig.colorbar(surface2, shrink=0.5, aspect=5)
# ax1.set_title('Wykres nowy')
# plt.savefig('wykres5.png')
# plt.show()
