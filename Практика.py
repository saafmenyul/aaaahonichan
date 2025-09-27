"""
c = float(input())
g = int(c)
if g % 2 == 0:
  print('Четное')
else:
  print('Нечетное')
if c > 0:
  print('Больше 0')
elif c == 0:
  print('Это 0')
else:
  print('Меньше 0')
if c >= 10 and c < 51:
  print('В диапозоне [10, 50]')
else:
  print('Не в диапозоне [10, 50]')
f = (c* 1.8) + 32
k = c + 273.15
print(round(f, 2))
print(round(k, 2))
"""


"""
import random

let = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
num = '0123456789'
sp = '!@#$%^&*'
l = random.choices(let, k=3)
n = random.choices(num, k=3)
s = random.choices(sp, k=2)
pas = l+n+s
random.shuffle(pas)
z = ''.join(pas)
print(z)
"""


"""
from collections import Counter
a = input()
a = a.lower()
coun = Counter(a)
for i, j in coun.items():
  print(f"'{i}': '{j}'")
t2 = sorted(coun.items(), key=lambda x: (-x[1], x[0]))[:3]
print('Топ 3:')
for i, j in t2:
  print(i)
"""


"""
n = int(input())
tf = [True] * n
fin = []
for i in range(2, n):
  if tf[i]:
    fin.append(i)
    for j in range(i, n, i):
      tf[j] = False
print(fin)
"""