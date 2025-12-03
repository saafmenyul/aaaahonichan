import random

# Выбираем три случайные заглавные буквы
letters = ''.join(random.choice("QWERTYUIOPASDFGHJKLZXCVBNM") for i in range(3))

# Выбираем три случайные цифры
digits = ''.join(random.choice("1234567890") for i in range(3))

# Выбираем два специальных символа
special_chars = ''.join(random.choice('!@#$%^&*') for i in range(2))

# Собираем все части в список
all_parts = [letters, digits, special_chars]

# Перемешиваем части
random.shuffle(all_parts)

# Объединяем в пароль
password = ''.join(all_parts)

print(password)
