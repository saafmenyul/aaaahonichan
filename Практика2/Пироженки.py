def print_pack_report(number):
    if number % 3 == 0 and number % 5 == 0:
        return f"{number} - расфасуем по 3 или по 5"
    elif number % 5 == 0 and number % 3 != 0:
        return f"{number} - расфасуем по 5"
    elif number % 3 == 0 and number % 5 != 0:
        return f"{number} - расфасуем по 3"
    else:
        return f"{number} - не заказываем!"


print(print_pack_report(int(input())))