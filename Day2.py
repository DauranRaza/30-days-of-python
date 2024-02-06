# Declare different variables and assign them values
# Declare multiple variables on one line

firstname, lastname, fullname, country, city = "Dauran", "Raza", "Dauran Raza", "Pakistan", "Kahuta"
age, year = 37, 1986
is_married, is_true, is_light_on = True, False, True

# check data type of all variables using type() builtin function

print("the type of firstname is", type (firstname))
print("the type of lastname is ", type (lastname))
print("the type of fullname is ", type (fullname))
print("the type of country is ", type (country))
print("the type of city is ", type(city))
print("the type of age is ", type (age))
print("the type of year  is ", type (year))
print("the type of is_married is ", type (is_married))
print("the type of is_true is ", type (is_true))
print("the type of is_light_on is ", type (is_light_on))

# using len() builtin function check length of first name variable

print("the length of firstname is ", len (firstname))

# compare length of first name and last name

if len(firstname) < len(lastname):
    print("Length of firstname is less than length of lastname")

elif len(firstname) == len(lastname):
    print ("length of lastname and firstname are equal")

else:
    print("length of firstname is greater than length of lastname")

# Declare num one and num two and apply operations

num_one, num_two = 5, 4

total = (num_one + num_two)
print("sum of two numbers is ", total)
diff = (num_one - num_two)
print("difference of two number is ", diff)
product = (num_two * num_one)
print("product of two numbers is ", product)
division = (num_one / num_two)
print("division of two number is ", division)
remainder = (num_two % num_one)
print("remainder of two numbers is ", remainder)
exp = (num_one**num_two)
print("exponential of two number is ", exp)
floor_div = (num_one // num_two)
print("floor division of two numbers is ", floor_div)

# radius of circle is 30 do some maths

import math
radius = 30
area =  (math.pi * (radius**2))
circum = 2 * math.pi * radius
print ("area of circle is ", area)
print ("circumference of circle is ", circum)

#take radius as input from user and calculate area and circumference

radius2 = int(input("Enter and Integer Number: "))
print(radius2)
area_2 = (math.pi * (radius2**2 ))
circum_2 = 2 * math.pi * radius2
print ("area of circle 2 is ", area_2)
print ("circumference of circle 2 is ", circum_2)
