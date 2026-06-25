x, y, z = input("Expression: ").strip().split(" ")
x = int(x)
z = int(z)

if y == "+":
    print((x) + (z))
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/" and z != 0:
    print(x / z)
else:
    print("Enter valid statement bruh!!")
