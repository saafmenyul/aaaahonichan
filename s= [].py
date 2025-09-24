s= []
d = []
f= 's'
z = ' '
while f != '0':
    f = input()
    f = f.replace(z, '')
    if f == '0':
        break
    s.append(f)
g=''
while g != 0:
    g = input()
    g = g.replace(z, '')
    if g not in s:
        d.append(g)
    else:
        s.remove(g)
    if g == '0':
        break
print('Есть во 2, но нет в 1', d)
print('Есть в 1, но нет во 2', s)