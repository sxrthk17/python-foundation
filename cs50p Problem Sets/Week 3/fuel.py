while True:
    try:
        fraction = input("Fraction: ").split("/")
        x, y = int(fraction[0]), int(fraction[1])
        if x <= y:
            fuel_percent = (x/y) * 100
            if fuel_percent <= 1:
                print("E")
            elif fuel_percent == 100:
                print("F")
            print(f"{fuel_percent:.0f} %")
            break
    except (ValueError, ZeroDivisionError):
        continue
