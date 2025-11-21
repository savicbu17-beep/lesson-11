class BankAccount:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance + amount
        print(f"{self.owner} ви поповннили на {amount} грн баланс {self.balance} грн")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance - amount
            print(f"{self.owner} знято {amount} грн Залишок {self.balance} грн")
        else:
            print(f"{self.owner} недостатньо коштів")

class Bank:
    def __init__(self):
        self.accounts = {}

    def add(self, acc):
        self.accounts[acc.number] = acc

    def transfer(self, from_num, to_num, amount):
        a1, a2 = self.accounts.get(from_num), self.accounts.get(to_num)
        if a1 and a2 and a1.balance > amount:
            a1.balance - amount
            a2.balance + amount
            print(f"Переказ {amount} грн з {a1.owner} до {a2.owner}")
        else:
            print("Помилка переказу")

# Приклад
b = Bank()
a1 = BankAccount("Ваня", "001", 5000)
a2 = BankAccount("Максім", "002", 3000)
b.add(a1)
b.add(a2)

a1.deposit(1000)
a2.withdraw(500)
b.transfer("001", "002", 2000)

print(f"{a1.owner} {a1.balance} грн")
print(f"{a2.owner} {a2.balance} грн")
