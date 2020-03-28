

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Mar"])
print(monthConversions.get("Jun", "Not a valid key"))    #--> Default Value

# todo can add a default value if its not not assignable keyword                         "dict_name.get("Key", "Default Value")"                           print(monthConversions.get("Jun", "Not a valid key"))














