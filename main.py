class Account():
    def __init__(self, id, balance=0, ):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет. Сумма на счету {self.balance}")


    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
            print(f"Вы успешно сняли {money}. Баланс {self.balance}")
        else:
            print(f"Денежный средств недостаточно. Вы запросили {money}, а на счете {self.balance}")

    def all_balance(self):
        print(f"Текущий баланс - {self.balance}")


man = Account("1234567", 600)

man.all_balance()
man.withdraw(300)
man.withdraw(800)
man.deposit(23000)
man.all_balance()