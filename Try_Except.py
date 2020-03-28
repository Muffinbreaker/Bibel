
"""
number = (input("Enter a number: "))
list =[]

list.append(number)


for i in list:

    try:
        print(float(i)*2)

    except:
        print("Dies ist keine Zahl!")
"""



try:
    answer = 10/0
    number = float((input("Enter a number: ")))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invailid input")



























































