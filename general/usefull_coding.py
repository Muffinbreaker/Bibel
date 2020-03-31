
condition = False

if condition:
    x = 1
else:
    x = 0

print(x)

# ---------------------------------->

condition_1 = False

y = 1 if condition_1 else 0

print(y)

# ---------------------------------->








num1 = 1_000_000_000_000
num2 = 1_000_000_000

total = float(num1 + num2)

print(f'{total:,}')   # todo ------> print the numbers seperated.

# todo ----------------------------------> u can use underscores to separate big numbers!









with open ("/home/muffinbreak/PycharmProjects/Bibel/general/file_projects/employees", "r") as f:
    file_contents = f.read()     # -----------> use countent manager to open files!!!

words = file_contents.split(" ")
word_count =len(words)
print(word_count)







index = 0
names = ["Corey", "Chris", "Dave", "Travis"]

for name in names:
    print(index, name)
    index += 1

# ---------------------------------->

for index, name in enumerate(names, start=1):
    print(index, name)

# todo .. alternate and effective way to count for loops!





names_2 = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
names_3 = ["Spiderman", "Superman", "Deadpool", "Batman"]
names_4 = ["Marvel", "DC", "Marvel", "DC"]


for index, name in enumerate(names_2):
    hero = names_3[index]
    print(name + " is actually " + hero)


for name, hero, universe in zip(names_2, names_3, names_4):
    print(name + " is actually " + hero + " played in the " + universe + " universe ")


# todo ---> alternative way to spell the index of 2 numbers!






# Unpacking Tuples

a, b, *_, d = (1, 2, 3, 4, 5)


print(a)
print(b)
#print(c)
print(d)

a, b, *c, d = (1, 2, 3, 4, 5)


print(a)

print(b)
print(c)
print(d)




#--------------------------------------------------------------------------->



