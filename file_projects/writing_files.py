"""
r = read
w = write
a = append
r+ = read and write
"""


employee_file = open("/home/muffinbreak/PycharmProjects/Bibel/file_projects/employees", "w")


employee_file.write("\nKelly - Customer Service")


employee_file.close()




# todo variable.write() can add another information to the data if u are in "a" append mode                                        --->    employee_file.write("Shit - in the Toilet")
# todo variable.write() use the /n to save the information in a new line!                                                          --->    employee_file.write("\nKelly - Customer Service")
# todo variable.write() if u are in "w" mode (write) u overwrite the hole data and just save the new input                         --->    employee_file.write("\nKelly - Customer Service")
# todo variable.write() u can also use the "w" (write) mode to crate completely new datas. U have to change the name.              --->    employee_file.write("\nKelly - Customer Service")



















