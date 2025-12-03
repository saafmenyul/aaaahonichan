def caesar_cipher(text, shift):
    """
    Применяет сдвиг к каждому символу, кроме пробела:
    - шифрует: сдвиг вперёд на заданный шаг
    - дешифрует: сдвиг назад на заданный шаг
    Возвращает кортеж: (зашифрованный_текст, расшифрованный_текст)
    """
    encrypted = ""   # Зашифрованная строка
    decrypted = ""   # Расшифрованная строка

    for char in text:
        if char != " ":
            encrypted += chr(ord(char) + shift)
            decrypted += chr(ord(char) - shift)
        else:
            encrypted += " "
            decrypted += " "

    return encrypted, decrypted


# Вводим данные
text = input()
shift = int(input())

# Применяем шифрование и дешифрование
encrypted_text, decrypted_text = caesar_cipher(text, shift)

# Выводим результат
print(f"Шифрованный текст: {encrypted_text}, "
      f"Дешифрованный текст: {decrypted_text}")
