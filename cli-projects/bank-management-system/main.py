from bank import Bank
## CLI BASED MAIN()
def main():



  bank = Bank("BANK1", "BANK1000909")
  while True:
    print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. View Account Details\n6. Exit\n")

    try:
      choice = int(input("Enter your choice: "))
      match choice:
        case 1:
          print("\nTo create account:")
          name = input("Enter your name: ").strip().title()

          try:
            balance = int(input("Enter initial balance(>500): ").strip())
            pin = int(input("Enter a 4-digit account pin: ").strip())
          except:
            print("Invalid Input\n")
            continue ## the loop continues without breaking

          acc_no = bank.create_account(name, balance, pin)

          if acc_no is None:
            print("Account creation failed!!\n")
          else:
            print(f"\nAccount created!")
            print(f"Account No: {acc_no}\n")

        case 2:
          print("\nDeposit Menu:")
          acc_no = input(f"Enter your {bank.bank_name} account number: ").strip().upper()
          if acc_no not in bank.accounts:
            print(f"No account with A/C number: {acc_no} found!\n")
            continue
          else:

            try:
              amount = int(input("Enter the amount you want to deposit: \n"))
            except:
              print("Invalid Amount\n")
              continue

            deposited = bank.deposit(acc_no, amount)
            if deposited:
              print("+-------------------------------+")
              print(f"Deposited {amount} successfully!")
              print("+-------------------------------+\n")
            else:
              print("Deposit Failure, check given amount!\n")
              continue

        case 3:
            print("\nWithdraw Menu:")
            acc_no = input(f"Enter your {bank.bank_name} account number: ").strip().upper()

            if acc_no not in bank.accounts:
              print(f"No account with A/C number: {acc_no} found!\n")
              continue

            try:
              amount = int(input("Enter the amount you want to withdraw: ").strip())
              pin = int(input("Enter you 4-digit PIN: ").strip())
            except:
              print("Invalid Input!\n")
              continue

            result = bank.withdraw(account_no= acc_no,
                                      amount= amount, pin= pin)

            if result: ## no need to use == True
              print("+---------------------------------------+")
              print(f" Rs.{amount} was withdrawn successfully!")
              print("+---------------------------------------+\n")
            else:
              print("\nWithdrawal Failure.\nCheck Amount/Pin.\n")
              continue

        case 4:
          print("\nChecking Balance Menu:")
          acc_no = input(f"Enter your {bank.bank_name} account number: ").strip().upper()

          try:
            pin = int(input("Enter your 4-digit PIN: ").strip())
          except:
            print("Invalid PIN\n")
            continue ## missed this last time

          acc_balance = bank.check_balance(acc_no, pin)

          if acc_balance == None:
            print("Invalid A/c number/ PIN\nTry Again Later.\n")
            continue ## missed this too
          
          print("Balance fetched successfully!\n")
          print("+---------------------------------------+")
          print(f"Account '{acc_no}' has balance Rs.{acc_balance}")
          print("+---------------------------------------+\n")

        case 5:
          print("\nAccount Detail Menu:")
          acc_no = input(f"Enter your {bank.bank_name} account number: ").strip().upper()

          try:
            pin = int(input("Enter your 4-digit PIN: ").strip())
          except:
            print("Invalid PIN\n")
            continue ## missed this last time

          acc_detail = bank.get_account_details(account_no= acc_no, pin=pin)

          if acc_detail == None:
            print("Invalid A/c or PIN.\nUnable to fetch A/c detail\n")
          else:
            print("+-----------------------------+")
            print(f"Account Details: ")
            print(f"Name: {acc_detail['name']}\nAccount No.: {acc_detail['account_no']}")
            print(f"IFSC Code: {bank.ifsc_code}")
            print(f"A/c balance: {acc_detail['balance']}")
            print("Transaction History")
            if len(acc_detail['transactions']) == 0:
              print("No Transaction History")
            else:
              for transaction in acc_detail['transactions']:
                print(transaction)
            print("+-----------------------------+\n")

        case 6:
          print("Thank you for banking with us.\nHave a great day!\n")
          break
        case _:
          print("Enter a valid choice!\n")
    except:
      print("Invalid Choice!\n") 
      continue
  print("Session closed\n")

if __name__ == "__main__":
  main()
