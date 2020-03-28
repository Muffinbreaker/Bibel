from math import *

name = (input("Welcher Zahl möchten Sie die Wurzel ziehen?"))
liste = []

liste.append(name)


for minus in liste:
    if minus.count("-"):
        print("Bitte geben sie eine Zahl größer 0 ein!")
        break
    elif minus.count(","):
        print("Benutzen sie Punkt statt Komma!")
        break


    for entry in liste:

        try:
            print(abs(sqrt(float(entry))))


        except:
            print("Bitte beachten Sie das Eingabeformat!")