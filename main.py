from math import *

#1

i, ii = 5, -7

c, cc = 6j + 3, 7j - 2

f, ff = 5.6, -8.3

string, sstring = "task", 'one'

print('Intiger No1 =', i, '\nIntiger No2 =', ii)
print('\nComplex No1 =', c, '\nComplex No2 =', cc)
print('\nFloat No1 =', f, '\nFloat No2 =', ff)
print('\nString No1 =', string, '\nString No2 =', sstring)

#2

addition = i + ii
subtraction = ii - i
multiplication = i * ii
division = ii / i

#3

x = 2
x += 1
x -= 2
x *= 2
x /= 0.5
x **= 2
x %= 5

#4

print('\n', exp(10))
print((log(5 + sin(8)**2))**1/6)
print(floor(3.55))
print(ceil(4.80))

#5

name = 'ADAM'
surname = 'TRENTOWSKI'

print('\n', name.capitalize(), surname.capitalize())

#6

frogsong = 're re re re kum kum kum re kum kum kum'

print('\n', frogsong.count('kum'))

#7

string7 = "Aklfsndl8#"

print('\n', string7[1])
print(string7[9])

#8

print('\n', frogsong.split())

#9

string9 = "abcde"
float9 = 5.8231
hexadecimal9 = 1213


print('\n', str(string9), float(float9), hex(hexadecimal9))






