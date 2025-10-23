class Transport:
    def __init__(self, name, speed=0, price=None):
        self.name = name
        self.speed = speed
        self.price = price
    

    def info(self):
        return f"Это {self.name}"


class Car(Transport):
    def info(self):
        if self.price:
            return f"{self.name} - ездит по дороге, со скоростью {self.speed} и стоит примерно {self.price}"
        else:
            return f"{self.name} - ездит по дороге, со скоростью {self.speed}"


class Plane(Transport):
    def info(self):
        if self.price:
            return f"{self.name} - летает в небе, со скоростью {self.speed} и стоит примерно {self.price}"
        else:
            return f"{self.name} - летает в небе, со скоростью {self.speed}"


class Boat(Transport):
    def info(self):
        if self.price:
            return f"{self.name} - плавает по воде, со скоростью {self.speed} и стоит примерно {self.price}"
        else:
            return f"{self.name} - плавает по воде, со скоростью {self.speed}"


t1 = Transport("транспорт")
t2 = Car("машина", 60, "2 миллиона рублей")
t3 = Plane("самолет", 821, "21,5 миллиона рублей")
t4 = Boat("лодка", 40)
print(t1.info())
print(t2.info())
print(t3.info())
print(t4.info())