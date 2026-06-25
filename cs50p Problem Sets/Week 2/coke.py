accepted_coins = [25, 10, 5]

amount_due = 50
while amount_due <= 50:
    print(f"Amount Due: {amount_due}")
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin in accepted_coins:
        amount_due -= inserted_coin
        if amount_due < 0:
            print(f"Change Owed: {abs(amount_due)}")
            break
        elif amount_due == 0:
            print(f"Change Owed: {amount_due}")
            break
    else:
        continue
