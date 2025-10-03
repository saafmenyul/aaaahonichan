n = int(input())
a = ''
c = 1
e = n
f = 1
while n > 0:
    a= str(c)
    n -= f
    c += 1
    if len(str(c)) != f:
        f += 1
print(int(a[(n-1) % f]))