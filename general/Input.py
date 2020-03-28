

i1 = int((input("Geben sie eine Zahl ein!")))
i2 = (input("Geben sie einen Rechenoperator ein!"))
i3 = int((input("Geben Sie eine weitere Zahl ein")))


if i2 == "+":
    print(int(i1 + i3))
elif i2 == "-":
    print(int(i1 - i3))
elif i2 == "/":
    print(int(i1 / i3))
elif i2 == "*":
    print(int(i1 * i3))
elif i2 == "^":
    print(int(pow(i1, i3)))


# todo --> open an input window                       "input("...........")"                                     print(input(".............."))
# todo --> input can be output in i variable          "name = input("........")                                  name = input("........")