num = float(input())
if num % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")
if num > 0:
    print("Число положительное")
elif num == 0:
    print("Это 0")
else:
    print("Число отрицательное")
if num > 9 and num < 51:
    print("Число входит в диапазон")
else:
    print("Число не входит в диапазон")
