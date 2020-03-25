

# string = "Hello"
# integer = 20
# True or False value "print(age == 100)"


name = "Oliver"
age = 100

print("There once was a man named " + name + ", ")
print("he was " + str(age) + " years old. ")

name = "Lucas"
print("He really liked the name " + name + ", ")
print("but didn't like being " + str(age) + ".")

# todo create a new line in a string -->                                        \n                                              print("Ich bin\nder beste!")
# todo create a " in a string line -->                                          \"                                              print("Ich bin\"der beste!")

phrase = "Ich bin der beste"

# todo convert the string in lower case letters                                 ".lower()"                                      print(phrase.lower())
# todo convert the string in capital letters                                    ".upper()"                                      print(phrase.upper())
# todo true or false value if the string is upper or not                        ".isupper()"                                    print(phrase.isupper())
# todo give me the exact length of an Value                                     "len()"                                         print(len(phrase))
# todo give me the choosen index                                                "[0])"                                          print(phrase[0])
# todo show me the first position from the choosen index                        ".index()"                                      print(phrase.index("b"))
# todo replace the first with the second atribute                               ".replace()"                                    print(phrase.replace("der", "die"))


print(phrase.upper().isupper())

print(phrase.replace("der", "die"))