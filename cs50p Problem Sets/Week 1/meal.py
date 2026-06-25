def main():
    time = input("What time is it? ")
    if ":" in time:
        convert(time)
    else:
        print("Invalid Time")


def convert(time):
    hour, minutes = time.split(":")
    hour, minutes = int(hour), int(minutes)
    if hour in [7, 8]:
        if hour != 8 and minutes in range(0, 60) or hour == 8 and minutes == 00:
            print("breakfast time")
    elif hour in [12, 13]:
        if hour != 13 and minutes in range(0, 60) or hour == 13 and minutes == 00:
            print("lunch time")
    elif hour in [18, 19]:
        if hour != 19 and minutes in range(0, 60) or hour == 19 and minutes == 00:
            print("dinner time")


if __name__ == "__main__":
    main()
