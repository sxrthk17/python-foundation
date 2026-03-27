import pytz
from datetime import datetime

india_timezone = pytz.timezone('Asia/Kolkata')
india_time = datetime.now(india_timezone)
print(india_time.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

now = datetime.now(india_timezone)
print(now)


class Account():
    def __init__(self, name, ac_no, balance, pin):  # remove transactions
        self.name = name
        self.ac_no = ac_no
        self.balance = balance
        self.pin = pin
        # when initialising the history is empty initialising it here..
        self.transactions = []

    def deposit(self, amount):
        now = datetime.now(india_timezone)
        if amount > 0:  # dont use self.amount its a parameter not an attribute
            self.balance += amount
            self.transactions.append(
                f"{now.strftime('%Y-%m-%d %H:%M:%S')}| Deposited: Rs.{amount}")
            return True
        else:
            return False  # oreturning false and let the bank make decision if amount is valid or not

    def withdraw(self, amount, pin):
        if pin != self.pin:
            return False
        else:
            if amount <= 0:
                return False
            if amount > self.balance:
                return False
            # not using else cause after all conditions are false we must goto withdraw..
            now = datetime.now(india_timezone)
            self.balance -= amount
            self.transactions.append(
                f"{now.strftime('%Y-%m-%d %H:%M:%S')}| Withdrawn: Rs.{amount}")
            return True
