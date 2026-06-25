def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s[0:2].isalpha() or s[2:4].isdigit():
        return False

    if not s.isalnum():
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            # If the first digit encountered is '0', it's invalid
            if s[i] == '0':
                return False

            if not s[i:].isdigit():
                return False

        break

    return True


main()
