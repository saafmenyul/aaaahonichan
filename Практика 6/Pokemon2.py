import requests


class PokemonTeamManager:
    """Класс для управления командой покемонов."""

    def __init__(self):
        """Инициализация менеджера команды."""
        self.team = []  # Список покемонов в команде
        self.api_url = "https://pokeapi.co/api/v2/pokemon/"

    def add_pokemon(self, name):
        """
        Добавляет покемона в команду.

        Args:
            name (str): Имя покемона для добавления

        Returns:
            bool: True если добавлен, False если уже есть в команде
        """
        # Проверяем, есть ли покемон уже в команде
        if name.lower() in [p['name'].lower() for p in self.team]:
            print(f"Покемон {name} уже есть в команде!")
            return False

        # Получаем данные покемона из API
        try:
            response = requests.get(f"{self.api_url}{name.lower()}")
            response.raise_for_status()
            data = response.json()

            # Сохраняем информацию о покемоне
            pokemon_info = {
                'name': data['name'],
                'hp': data['stats'][0]['base_stat'],
                'attack': data['stats'][1]['base_stat'],
                'defense': data['stats'][2]['base_stat'],
                'types': [t['type']['name'] for t in data['types']]
            }

            self.team.append(pokemon_info)
            print(f"Покемон {name} добавлен в команду!")
            return True

        except requests.exceptions.RequestException:
            print(f"Покемон {name} не найден!")
            return False

    def remove_pokemon(self, name):
        """
        Удаляет покемона из команды.

        Args:
            name (str): Имя покемона для удаления

        Returns:
            bool: True если удален, False если не найден
        """
        # Ищем покемона в команде
        for i, pokemon in enumerate(self.team):
            if pokemon['name'].lower() == name.lower():
                removed = self.team.pop(i)
                print(f"Покемон {removed['name']} удален из команды!")
                return True

        print(f"Покемон {name} не найден в команде!")
        return False

    def view_team(self):
        """Выводит подробную информацию обо всех покемонах в команде."""
        if not self.team:
            print("Команда пуста!")
            return

        print("\n=== Ваша команда ===")
        for i, pokemon in enumerate(self.team, 1):
            print(f"\n{i}. {pokemon['name'].upper()}")
            print(f"   HP: {pokemon['hp']}")
            print(f"   Атака: {pokemon['attack']}")
            print(f"   Защита: {pokemon['defense']}")
            print(f"   Типы: {', '.join(pokemon['types'])}")

    def find_pokemon(self, name):
        """
        Находит покемона в команде по имени.

        Args:
            name (str): Имя покемона для поиска

        Returns:
            dict or None: Информация о покемоне или None
        """
        # Ищем покемона в команде
        for pokemon in self.team:
            if pokemon['name'].lower() == name.lower():
                print(f"\n=== {pokemon['name'].upper()} ===")
                print(f"HP: {pokemon['hp']}")
                print(f"Атака: {pokemon['attack']}")
                print(f"Защита: {pokemon['defense']}")
                print(f"Типы: {', '.join(pokemon['types'])}")
                return pokemon

        print(f"Покемон {name} не найден в команде!")
        return None

    def list_all_pokemon(self, limit=50):
        """
        Выводит список всех доступных покемонов из API.

        Args:
            limit (int): Количество покемонов для отображения
        """
        try:
            # Получаем список покемонов из API
            response = requests.get(
                f"{self.api_url}?limit={limit}"
            )
            response.raise_for_status()
            data = response.json()

            # Выводим список покемонов
            print(f"\n=== Список покемонов (показано {len(data['results'])} из {data['count']}) ===")
            for i, pokemon in enumerate(data['results'], 1):
                print(f"{i}. {pokemon['name'].capitalize()}")

            print(f"\nВсего доступно покемонов: {data['count']}")
            print("Для добавления введите имя покемона из списка.")

        except requests.exceptions.RequestException:
            print("Ошибка при получении списка покемонов!")

    def training_battle(self, name1, name2):
        """
        Устраивает тренировочный бой между двумя покемонами.

        Args:
            name1 (str): Имя первого покемона
            name2 (str): Имя второго покемона
        """
        # Находим покемонов в команде
        pokemon1 = None
        pokemon2 = None

        for pokemon in self.team:
            if pokemon['name'].lower() == name1.lower():
                pokemon1 = pokemon
            if pokemon['name'].lower() == name2.lower():
                pokemon2 = pokemon

        # Проверяем, что оба покемона найдены
        if not pokemon1:
            print(f"Покемон {name1} не найден в команде!")
            return

        if not pokemon2:
            print(f"Покемон {name2} не найден в команде!")
            return

        # Вычисляем силу покемонов (простая формула)
        power1 = pokemon1['hp'] + pokemon1['attack'] + pokemon1['defense']
        power2 = pokemon2['hp'] + pokemon2['attack'] + pokemon2['defense']

        # Определяем победителя
        print(f"\n=== Тренировочный бой ===")
        print(f"{pokemon1['name'].upper()} (сила: {power1}) vs "
              f"{pokemon2['name'].upper()} (сила: {power2})")

        if power1 > power2:
            print(f"Победитель: {pokemon1['name'].upper()}!")
        elif power2 > power1:
            print(f"Победитель: {pokemon2['name'].upper()}!")
        else:
            print("Ничья!")


def main():
    """Главная функция с интерактивным меню."""
    manager = PokemonTeamManager()

    print("Добро пожаловать в менеджер команды Pokémon!\n")

    # Основной цикл программы
    while True:
        # Выводим меню
        print("\n=== МЕНЮ ===")
        print("1. Добавить покемона в команду")
        print("2. Удалить покемона из команды")
        print("3. Просмотреть команду")
        print("4. Найти покемона по имени")
        print("5. Тренировочный бой")
        print("6. Список всех покемонов")
        print("7. Выход")

        # Получаем выбор пользователя
        choice = input("\nВыберите действие (1-7): ").strip()

        # Обрабатываем выбор
        if choice == "1":
            # Добавление покемона
            name = input("Введите имя покемона: ").strip()
            if name:
                manager.add_pokemon(name)
            else:
                print("Имя не может быть пустым!")

        elif choice == "2":
            # Удаление покемона
            name = input("Введите имя покемона для удаления: ").strip()
            if name:
                manager.remove_pokemon(name)
            else:
                print("Имя не может быть пустым!")

        elif choice == "3":
            # Просмотр команды
            manager.view_team()

        elif choice == "4":
            # Поиск покемона
            name = input("Введите имя покемона для поиска: ").strip()
            if name:
                manager.find_pokemon(name)
            else:
                print("Имя не может быть пустым!")

        elif choice == "5":
            # Тренировочный бой
            name1 = input("Введите имя первого покемона: ").strip()
            name2 = input("Введите имя второго покемона: ").strip()
            if name1 and name2:
                manager.training_battle(name1, name2)
            else:
                print("Оба имени должны быть указаны!")

        elif choice == "6":
            # Список всех покемонов
            limit_input = input("Сколько покемонов показать? (по умолчанию 50): ").strip()
            if limit_input.isdigit():
                manager.list_all_pokemon(int(limit_input))
            else:
                manager.list_all_pokemon()

        elif choice == "7":
            # Выход из программы
            print("До свидания!")
            break

        else:
            print("Неверный выбор! Попробуйте снова.")


if __name__ == "__main__":
    main()
