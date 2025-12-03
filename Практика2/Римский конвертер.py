# Определяем константы для работы с римскими числами
all_roman  = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]
check = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

# Выводим меню выбора направления перевода
print("Из какой системы в какую надо перевести?")
print("Из римской в десятичную введите: 1")
print("Из десятичной в римскую введите: 2")

# Получаем выбор пользователя
choice = int(input())

# Проверяем корректность выбора
if choice != 1 and choice != 2:
    print("Вы ввели что-то не то")

# Если выбрана конвертация из римской в десятичную
if choice == 1:
    is_valid = True
    
    print("Введите число в формате: XXIC")
    roman_number = input()
    
    # Проверяем, что все символы - допустимые римские цифры
    for char in roman_number:
        if char not in check:
            is_valid = False
            print("Вы ввели что-то не то")
            break
    
    # Если число корректное, конвертируем
    if is_valid:
        decimal_result = 0
        index = 0
        
        # Проходим по римскому числу и переводим в десятичное
        while index < len(roman_number):
            for value, roman_digit in all_roman:
                if roman_number[index:index+len(roman_digit)] == roman_digit:
                    decimal_result += value
                    index += len(roman_digit)
                    break
        
        print(decimal_result)

# Если выбрана конвертация из десятичной в римскую
else:
    is_valid = True
    
    print("Введите число в формате: 12312")
    decimal_input = input()
    
    # Проверяем, что введены только цифры (не римские символы)
    for char in decimal_input:
        if char in check:
            print("Вы ввели что-то не то")
            is_valid = False
            break
    
    # Если число корректное, конвертируем
    if is_valid:
        roman_result = ''
        number = int(decimal_input)
        
        # Конвертируем десятичное число в римское
        for value, roman_digit in all_roman:
            while number >= value:
                roman_result += roman_digit
                number -= value
        
        print(roman_result)
