def print_pack_report(number):
    # Функция определяет, как можно расфасовать товар в упаковки.
    
    # Если число делится и на 3, и на 5
    if number % 3 == 0 and number % 5 == 0:
        return f"{number} - расфасуем по 3 или по 5"
    
    # Если число делится только на 5
    elif number % 5 == 0 and number % 3 != 0:
        return f"{number} - расфасуем по 5"
    
    # Если число делится только на 3
    elif number % 3 == 0 and number % 5 != 0:
        return f"{number} - расфасуем по 3"
    
    # Если число не делится ни на 3, ни на 5
    else:
        return f"{number} - не заказываем!"


# Получаем число от пользователя и выводим результат
print(print_pack_report(int(input("Введите количество товара: "))))
