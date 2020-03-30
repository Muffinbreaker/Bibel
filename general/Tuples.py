

coordinates = (1, 2, 3, 4, 5, 6, 7)


print(coordinates)



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


student = ("Max Müller", 22, "Informatik")    #number of information must match number of elements

name, age, subject = student

print(name)


# todo A Tuple is a collection of Python objects separated by commas. In someways a tuple is similar to a list in
#  terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable.

# todo tuples are used for data that never will be changed!