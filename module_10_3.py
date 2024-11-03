import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = int()
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            rand = random.randint(50, 500)
            self.balance += rand
            print(f'Пополнение: {rand}. Баланс: {self.balance}')
        if self.balance >= 500 and self.lock.locked():
            self.lock.release()
        time.sleep(0.001)

    def take(self):
        for i in range(100):
            rand = random.randint(50, 500)
            print(f'Запрос на {rand}')
            if rand <= self.balance:
                self.balance -= rand
                print(f'Снятие: {rand}. Баланс: {self.balance}')
            elif rand > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')