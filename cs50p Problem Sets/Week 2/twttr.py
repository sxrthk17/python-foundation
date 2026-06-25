input_str = input("Input: ")

print("Output: ", end="")
for char in input_str:
    if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
        print(char, end="")
    else:
        continue

print()
