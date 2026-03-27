from account import Account
class Bank:
  def __init__(self, bank_name, ifsc_code):
    self.bank_name = bank_name
    self.ifsc_code = ifsc_code
    self.accounts = {}
    self.next_acc_no = 1001 ## controlled uniqueness

  def create_account(self, name, balance, pin):
    if balance < 500:
      return None
    if not (1000 <= pin <= 9999):
      return None


    account_no = f"{self.bank_name}{self.next_acc_no}" #create
    account = Account(name, account_no, balance, pin)
    self.accounts[account_no] = account ##store
    self.next_acc_no += 1
    return account_no

  def deposit(self, account_no, amount):
    if account_no not in self.accounts:
      return False

    account = self.accounts[account_no]
    return account.deposit(amount)

  def withdraw(self, account_no, amount, pin):
    if account_no not in self.accounts:
      return False

    account = self.accounts[account_no]
    return account.withdraw(amount, pin)

  def check_balance(self, account_no, pin):
    if account_no not in self.accounts:
      return None

    account = self.accounts[account_no]

    if account.pin != pin:
      return None
    return account.balance

  def get_account_details(self, account_no, pin):
    if account_no not in self.accounts:
      return None
    account = self.accounts[account_no]
    if account.pin != pin:
      return None
    return {
        "name": account.name,
        "account_no":account.ac_no,
        "balance":account.balance,
        "transactions":account.transactions.copy() #not list reference bruh
    }
