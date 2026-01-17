class BankAccount:
    '''Основной класс'''
    def __init__(self, name, start_balance=0):
        self.name = name
        self.balance = start_balance
    

    def show_balance(self):
        print(f"У пользователя с именем - {self.name} на балансе: {self.balance} рублей")


class Operations:
    '''Базовый класс для всех операций'''
    def __init__(self, money):
        self.money = money
        self.done = False


    def do(self, account):
        pass

    
    def undo(self, account):
        pass


class Deposit(Operations):
    '''Класс для пополнения денег на счет'''
    def do(self, account):
        if not self.done:
            account.balance += self.money
            self.done = True
            print(f"Баланс пополнен на {self.money} рублей.")


    def undo(self, account):
        if self.done:
            account.balance -+ self.money
            self.done = False
            print(f"Отмена операции на {self.money} рублей")


class Withdrawal(Operations):
    '''Класс для снятие денег со счета'''
    def do(self, account):
        if not self.done:
            if account.balance >= self.money:
                account.balance -= self.money
                self.done = True
                print(f"С баланса снято {self.money} рублей.")
    

    def undo(self, account):
        if self.done:
            account.balance += self.money
            self.done = False
            print(f"Отмена операции на {self.money} рублей")


class Transfer(Operations):
    '''Класс для перевода денег между счетами'''
    def __init__(self, money, from_account, to_account):
        super().__init__(money)
        self.from_account = from_account
        self.to_account = to_account


    def do(self, account):
        if not self.done:
            if self.from_account.balance >= self.money:
                self.to_account.balance += self.money
                self.from_account.balance -= self.money
                self.done = True
                print(f"Переведено {self.money} от {self.from_account.name} к {self.to_account.name}")


    def undo(self, account):
        if self.done:
            self.to_account.balance -= self.money
            self.from_account.balance += self.money
            self.done = False
            print(f"Отмена операции на {self.money} рублей")


class InterestAccrual(Operations):
    '''Класс для начисления процентов'''
    def __init__(self, percent):
        super().__init__(0)
        self.percent = percent

    
    def do(self, account):
        if not self.done:
            added = account.balance * self.percent/100
            self.money = added
            account.balance += added
            self.done = True
            print(f"Начислено процентов на сумму {self.money} рублей")
    

    def undo(self, account):
        if self.done:
            account.balance -= self.money
            self.done = False
            print(f"Отмена операции на {self.money} рублей")


account1 = BankAccount("Иван", 1000)
account2 = BankAccount("Олег", 2000)
account1.show_balance()
op1 = Deposit(200)
op1.do(account1)
op1 = Withdrawal(250)
op1.do(account1)
account1.show_balance()
op1.undo(account1)
account1.show_balance()
op1 = Transfer(100, account1, account2)
op1.do(account1)
account1.show_balance()
account2.show_balance()
op1.undo(account1)
account1.show_balance()
account2.show_balance()
op1 = InterestAccrual(10)
op1.do(account1)
account1.show_balance()
op1.undo(account1)
account1.show_balance()
