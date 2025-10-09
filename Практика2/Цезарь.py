def f(text, shift):
    new_text = ""
    new_text_desh = ""
    for char in text:
        if char != " ":
            new_text += chr(ord(char) + shift)
            new_text_desh += chr(ord(char) - shift)
        else:
            new_text += " "
            new_text_desh += " "
    return new_text, new_text_desh


text = input()
shift = int(input())
result = []
for i in f(text, shift):
    result.append(i)
print(f"Шифрованный текст: {result[0]}, Дешифрованный текст: {result[1]}")
