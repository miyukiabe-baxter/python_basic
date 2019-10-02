######## Python String ########
# # print("Miyuki Abe")
# print("o----")
# print(" |||||")
# print('*' * 10)

# price = 10
# rating = 4.9
# name = 'Abe'
# is_published = True
# print(is_published)


# is_newPatient = True

# name = input('What is your name? ')
# fav_color = input('What is your favorite color? ')
# print('Hi ' + name + '. I heard your favorite color is ' + fav_color)
# print(name, 'is', age, 'and', is_newPatient)

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(type(age))
# print(age)

# your_weight = input('What is your weight in lb? ')
# your_weight_kg = float(your_weight) * 0.453592
# print(type(your_weight_kg))
# print('Your weight in Kg is %d' % (your_weight_kg))
# print('Your weight in Kg is', your_weight_kg)
# print('Your weight in Kg is' + str(your_weight_kg))

# course = 'Python for Beginners'
# print(course[1:-1])


# first = 'John'
# last = 'Smith'

# # print(first + ' [' + last + '] ' + 'is a coder')
# print(f'{first} [{last}] is a coder')

# course = 'Python for begineer'
# new_str = course.replace('begineer', 'absolute begineers')
# print(course)
# print(new_str)
# print('Python' in course)


######## Python Integer ########
# import math
# print(10/3)
# print(10 % 3)
# print(10 ** 3)  # exponent. 10 * 10 * 10

# x = 10.9
# y = -10
# print(round(x))
# print(abs(-x))

# print(f'ceiling of 5.5 is {math.ceil(5.5)}')
# print(f'ceiling of 5.5 is {math.floor(5.5)}')

######## Conditional ########

# if it is hot day
#   it's a hot day
#   Drink plenty of water
# otherwise if it is cold
#   it is a cold day
#   Wear warm clothes
# otherwise
#   it's a lovely day

# is_hot = False
# is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print("Drink a lot of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print('Enjoy your day')

# has_good_credit = False
# msg = 'Your down payment is '

# price = 1000000
# if has_good_credit:
#     downpayment = 0.1 * price
# else:
#     downpayment = 0.2 * price
# print(f'Your down payment will be ${int(downpayment)}')

### multiple conditions ######
# if applicant has high income AND good credit
#  Eligible for loan
# else not Eligible

# is_high_income = True
# has_good_credit = False
# has_criminal_record = True

# if is_high_income and not has_criminal_record:
#     print('Eligible for load')
# else:
#     print('Oops')

##comparison ######

# temp = 30

# if temp == 30:
#     print('It is a hot day')
# else:
#     print('it is not hot day')

# name = input('what is your name? ')

# if len(name) < 3:
#     print('name must be at least 3 characters')
# elif len(name) > 50:
#     print('name can be a maximum of 50 characters')
# else:
#     print('name looks good!')

# weight = int(input('Weight: '))
# l_or_k = input('(L)bs or (K)g: ')

# if l_or_k == 'l' or l_or_k == 'L':
#     print(f'{weight * 0.453592} kg')
# else:
#     print(f'{weight / 0.453592} lb')

# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# print('Done Done Done')

############### Guessing game ###############
# secret_num = 9
# num_of_guess = 0

# while num_of_guess < 3:
#     guess_num = int(input('Guess the number! '))
#     num_of_guess += 1
#     if num_of_guess <= 3 and guess_num == secret_num:
#         print('Your are correct!!')
#         break

# if num_of_guess < 3:
#     print('You win!!!')
# else:
#     print('You lost!!!')

# menu = ""
# is_started = False

# while True:
#     menu = input("> ").lower()
#     if menu == 'start':
#         if is_started:
#             print('Car is already started...')
#         else:
#             is_started = True
#             print('Car started')
#     elif menu == 'stop':
#         if not is_started:
#             print('Car has already stopped')
#         else:
#             is_started = False
#             print('Car has stopped')
#     elif menu == 'help':
#         print("""
#   start - to start the car
#   stop - to stop the car
#   quit - to exit""")
#     elif menu == 'quit':
#         break
#     elif menu == "":
#         print('You did not specify the menu')
#     else:
#         print('I do not understand that...')

# print('Quiting')


######## for loop ########

# for item in ['Miyuki', 'Billy', 'Kochi']:
#     print(item)

# for item in [1, 2, 3, 4, 5]:
#     print(item)

# for item in range(5, 10):
#     print(item)

# for item in range(5, 10, 2):
#     print(item)

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total cost is ${total}")

# for x in range(3):
#     for y in range(3):
#         print(f'({x}, {y})')

# numbers = [2, 2, 2, 2, 5]
# for num in numbers:
#     tempStr = ""
#     for i in range(num):
#         tempStr += "X"
#     print(tempStr)


###### list #####
# names = ['John', 'Bob', 'Miyu', 'Billy', 'Kochi']
# names[0] = 'Jon'
# print(names[:])

# num_list = [1, 6, 3, 8, 9, 90, 10, 3, 5, 40]
# largest = num_list[0]

# for num in num_list:
#     if largest < num:
#         largest = num
# print(largest)


###### 2D list #######
##numbers = [5, 2, 5, 5, 5, 5, 7, 4, 5, 6, 8, 9, 8]
# print(numbers)
# i = 0
# while i < len(numbers):
#     j = 0
#     while j < len(numbers):
#         if i != j and numbers[i] == numbers[j]:
#             numbers.remove(numbers[j])
#         j += 1
#     i += 1
# print(numbers)
# print(50 in numbers)
# numbers.remove(numbers[2])
# print(numbers)
# print(numbers.count(5))
# print(numbers.index(5))
# numbers.sort()  # in-place sort. therefore, this does not return new array.
# # if you wanna see the result, you need to print the original array
# numbers.reverse()  # reversing the sorted array
# numbers2 = numbers.copy  # making copy. javascript numbers2 = [...numbers]
# print(numbers)

# numbers = [5, 2, 5, 5, 5, 5, 7, 4, 5, 6, 8, 9, 8]
# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print(unique)

# Tuples #####  immutable data
# numbers = [1, 2, 3, 4, 5]  # mutable. I can access to append, pop,,,etc method.
# # this is immutable. so cannot access to methods which change the array.
# immutable_nums = (1, 2, 3, 4, 5)
# print(immutable_nums.count(1))

# coordinates = (1, 2, 3)
# # we can re-assign like below or
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# unpack like below
# x, y, z = coordinates
# print(x, y, z)

### dictonary - key value pair - Object - Map....etc ###
# customer = {
#     "name": "Miyuki",
#     "age": 32,
#     "is_verified": True
# }
# print(customer["name"])
# print(customer.get("name")) ## does not return error when "name" does not exist
# # if birthday does not exist, provide Aug 9th as a default
# print(customer.get('birthday', 'Aug 9th'))
# customer["name"] = "Billy"  # updating info.
# customer["birthday"] = "July 19th"  # adding key-value
# print(customer)

# numbers_list = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine"
# }

# user_phone_number = input("Phone: ")
# user_number = ""

# for num in user_phone_number:
#     user_number += f'{numbers_list.get(num, "No")}-'
# print(user_number[:-1])

### Emoji Converter ###


# def emoji_converter(message):
#     words = message.split(' ')
#     emoji = {
#         ":)": "😆",
#         ":(": "😢"
#     }

#     finalWord = ""
#     for word in words:
#         finalWord += emoji.get(word, word + " ")

#     return finalWord


# print(emoji_converter(input("> ")))


# Function ##### In Python, we use "def" to define function. not function


# def greet_user(first_name="Bob", last_name="B"):
#     print(f'Hi there {last_name}, {first_name}!!!!')
#     print('Welcome')


# print("start")
# greet_user('Miyuki', "Abe")
# greet_user()
# print("finish")

# def square(number):
#     return number * number


# print(square(3))

###### handling error ######
# try:
#     age = int(input('Age: '))
#     income = 50000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0')
# except ValueError:
#     print('Invalid value')
# except:  # every other error goes into this block
#     print('Something went wrong')


### Class ######

# class Point:
#     def __init__(self, x, y):  # this is equivalent to constructor. initializing an object
#         self.x = x
#         self.y = y

#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")


# point1 = Point(101, 8)
# print(point1.x)
# point1.move()
# point1.draw()

# print(point1)
# point2 = Point(1, 3)

# print(f'point1.x is {point1.x}. point2.x is {point2.x}')

# class Person:
#     def __init__(self, first_name, last_name, gender, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.gender = gender
#         self.age = age

#     def introduce_self(self):
#         print(f'Hi! My name is {self.first_name}. Nice to Meet you')


# miyuki = Person('miyuki', 'abe', 'f', 32)
# miyuki.introduce_self()

### Class inheritance ####
# class Mammal:
#     def walk(self):
#         print("walk")


# class Dog(Mammal):
#     # pass if we are not putting anyting, we say "pass"
#     def bark(self):
#         print("bark")


# class Cat(Mammal):
#     pass


# test_cat = Cat()
# test_cat.walk()
# # test_cat.bark()  # cat does not have bark method.

# test_dog = Dog()
# test_dog.bark()

#### module ####
# import utility <-- everything is accessible
# from utility import lbs_to_kg  # <--if you wann import specific one

# from utility import lbs_to_kg
# from utility import find_max
# import utility

# print(utility.kg_to_lbs(45))
# print(lbs_to_kg(100))

# print(find_max([3, 2, 7, 9, 3]))

### what is a package? ###
# imagine department store. we have women, men, children section.
# we write different modules for each section but as a whole, it is e-commerce site and it is one package.
# we can organize "python package with specific file name convention"
# create package folder "package_example". Then, create a file name "__init__.py"
# I can import them like,,,,,
###from package_example.woman import woman_clothes
###import package_example.woman

# built in module #### Detail is in python 3 module index
# we can access to build in modules like generating random number
# import random

# for i in range(3):
#     print(random.random())

# for i in range(3):
#     print(random.randint(10, 20))

# members = ['Miyu', 'Billy', 'Kochi']
# leader = random.choice(members)
# print(leader)

# import random


# class Dice:
#     def roll(self):
#         x = random.randint(1, 6)
#         y = random.randint(1, 6)
#         return x, y  # as a defult, Python thinks it is Tuples. if you want list, need to wrap with []


# test_dice = Dice()
# print(test_dice.roll())

# from pathlib import Path

# Absolute path : full address. Possible that the file is in the internet
# Relative path : the file has to be on local.

# Path class takes direcotry as an argument. as a defult, it takes current directory.
# path = Path()
# path1 = Path('package_example1')

# To create "email" directory, pass it as an argument and say mkdir on the returned object
# path2 = Path('emails')
# Path('another').mkdir()
# path2.mkdir()
# path2.rmdir()

# print(path.exists())
# print(path1.exists())

# path.glob('*.py')  # all python file list
# path.glob('*')  # all file
# path.glob('*.js')  # all JS file

# for file in path.glob('*'):
#     print(file)

## Installing Pipy package as a practice ##
