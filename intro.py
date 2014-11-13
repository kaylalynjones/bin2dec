age = 20
gender = 'female'

if age >= 21 and (gender == 'female' or gender == 'male'):
    print('go have a drink')
else:
    print('go have your parents buy you a drink')

for x in range(20, -50, -5):
    print("{0} to the {1} power is {2}".format(x, 2, x**2))

evens = []
for x in range(0, 20, 2):
    for y in range(3, 15, 3):
        if x == 10:
            evens.append((x, x ** 2, y, y ** 3, x * y))

def sum(a, b):
    return a + b

print(sum(3, 4))

#from math import pi
import math
def volume(r, h):
    return math. pi * r * r**2 * h

print(volume(3, 10))

# binary to decimal
def bin2dec(bin):
    sum = 0
    for index, bit in enumerate(bin[::-1]):
        sum += int(bit) * (2**index)
    return sum


dec = bin2dec('1101')
print(dec)
a = 4
