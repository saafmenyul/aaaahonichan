from collections import Counter

# Получаем строку от пользователя
text = input().lower()

# Подсчитываем количество каждого символа
char_count = Counter(text)

# Находим 3 самых частых символа (пузырьковая сортировка)
pairs = list(char_count.items())

# Простая сортировка пузырьком
for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        if pairs[i][1] < pairs[j][1]:  # Сравниваем количества
            pairs[i], pairs[j] = pairs[j], pairs[i]  # Меняем местами

most_common = pairs[:3]

# Выводим список всех символов
print("\nКоличество каждого символа:")
for char, count in sorted(char_count.items()):
    print(f"'{char}': {count}")

# Выводим 3 самых частых символа
print("Три самых частых символа:")
for char, count in most_common:
    print(f"'{char}': {count}")
