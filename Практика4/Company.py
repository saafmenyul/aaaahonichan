class Employee:
    def __init__(self, name, base_salary, bonus=0):
        self.name = name
        self.base_salary = base_salary
        self.bonus = bonus
    
    def calculate_salary(self):
        return self.base_salary + self.bonus


class Manager(Employee):
    def calculate_salary(self):
        return self.base_salary * 1.2 + self.bonus


class Developer(Employee):
    def calculate_salary(self):
        return self.base_salary * 1.1 + self.bonus


employee1 = Employee("Иван", 50000)
employee2 = Employee("Мария", 50000, 5000)
manager1 = Manager("Анна", 60000)
manager2 = Manager("Дмитрий", 60000, 15000)
developer1 = Developer("Петр", 55000)
developer2 = Developer("Ольга", 55000, 8000)
print(f"{employee1.name}: {employee1.calculate_salary()} руб.")
print(f"{employee2.name}: {employee2.calculate_salary()} руб.")
print(f"{manager1.name}: {manager1.calculate_salary()} руб.")
print(f"{manager2.name}: {manager2.calculate_salary()} руб.")
print(f"{developer1.name}: {developer1.calculate_salary()} руб.")
print(f"{developer2.name}: {developer2.calculate_salary()} руб.")