

#weight = float(input("How many pounds does your suitcase weigh? "))

#if weight > 50:
#    print("There is a $25 charge for luggage that heavy.")
#    print("Thank you for your business.")


#temperature = float(input('What is the temperature? '))

#if temperature > 70:
#    print('Wear shorts.')
#else:
#    print('Wear long pants.')
#    print('Get some exercise outside.')


is_male = True
is_tall = False


if is_male and is_tall:
    print("You are male and Tall!")

elif is_male and not(is_tall):
    print("You are male but short!")

elif not (is_male) and is_tall:
    print("You are not male but you are tall")

else:
    print("You are not male and tall")



def max_mum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_mum(100, 40434, 30492134))

# todo  == 2 values are equal
# todo  != 2 values are not equal
# todo  > bigger
# todo  < smaller
# todo  >= bigger or equal
# todo  <= smaller or equal

# todo The expression A "and" B is true if both A is true and B is true, and false if either is false. (For example, you get wet if it rains and you forgot your umbrella.)

#todo The expression A "or" B is true if either A is true or B is true, and false if both are false. (For example, school is closed if it is a holiday or it is a weekend.)

# todo The expression "not" A is true if A is false, and false if A is true. (For example, you are hungry if you have not eaten lunch.)











