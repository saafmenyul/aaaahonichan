n = int(input())
length = 1
count = 9
start = 1
while n > length * count:
    n -= length * count
    length += 1
    count *= 10
    start *= 10
num = start + (n - 1) // length
a = str(num)
final = a[(n - 1) % length]
print(final)
