"""
r = read
w = write
a = append
r+ = read and write
"""


employee_file = open("/file_projects/employees", "r")

for employee in employee_file.readlines():
    print(employee)


employee_file.close()

# todo variable.readable() give us the information if we are in read "r" mode!                                --->    print(employee_file.readable())
# todo variable.read() spit up all information from the data                                                  --->    print(employee_file.read())
# todo variable.readline() read the first line from the data.                                                 --->    print(employee_file.readline())
# todo variable.readline() put the informations in a list. You can choose the index u want                    --->    print(employee_file.readlines()[1)





