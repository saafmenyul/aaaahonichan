n = int(input())
numbers = [i for i in range(n + 1)]

numbers[1] = 0  # 1 не является простым числом

i = 2
while i <= n:
    if numbers[i] != 0:  # если число не вычеркнуто
        j = i + i  # начинаем с первого кратного
        while j <= n:
            numbers[j] = 0  # вычеркиваем кратные
            j += i  # следующее кратное
    i += 1

# Преобразуем в множество и удаляем нули
prime_numbers = set(numbers)
prime_numbers.remove(0)

print(prime_numbers)
