# Day 2: 30 Days of python programming 

firstName = 'Ben'
lastName = 'Manu'
full_name = firstName + lastName
coutry = 'Ghana'
city = 'Accra'
age = 18
year = 2024
is_married = False 
is_true = True 
is_light_on = True
occupation, industry, experience = 'tutor', 'IT Education', 4

'''Check the data type of all your variables using type() built-in function'''
print(type(firstName))
print(type(lastName))
print(type(full_name))
print(type(coutry))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(occupation))
print(type(industry))
print(type(experience))

'''Using the len() built-in function, find the length of your first name'''
print('lenght of variable',len(firstName))

'''Compare the length of your first name and your last name'''
print(len(firstName), len(lastName))

num_one, num_two = 5, 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

import math
radius = 30
area_of_circle = math.pi * radius ** 2
circumference = 2 * math.pi * radius
'''Take radius as user input and calculate the area.'''
radius = float(input('Enter radius: '))
area_of_circle = math.pi * radius ** 2

'''Use the built-in input function to get first name, last name, 
    country and age from a user and store the value to their 
    corresponding variable names'''

firstName = str(input('Enter first name: '))
lastName = str(input('Enter last name: '))
age = str(input('Enter age: '))

print(help('keywords'))