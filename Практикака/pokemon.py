import requests

# Получаем список первых 20 покемонов
response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=20')
pokemon_list = response.json()

# Извлекаем имена покемонов
names = [pokemon['name'] for pokemon in pokemon_list['results']]

# Выводим список имен
print("Список первых 20 покемонов:")
for name in names:
    print(f"  - {name}")

# Запрашиваем имя покемона у пользователя
pokemon_name = input("\nИмя покемона: ").lower()

# Получаем полную информацию о выбранном покемоне
response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/')
pokemon_data = response.json()

# Извлекаем и выводим данные
print(f"\nИмя: {pokemon_data['name']}")

# Типы покемона
types = [type_info['type']['name'] for type_info in pokemon_data['types']]
print(f"Тип: {', '.join(types)}")

print(f"Вес: {pokemon_data['weight'] / 10} кг")
print(f"Рост: {pokemon_data['height'] / 10} м")

# Способности
abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
print(f"Способности: {', '.join(abilities)}")
