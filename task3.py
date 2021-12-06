# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_USERNAME!")

def username():
    print("hello_USERNAME!")

while True:
    response = input("Type USERNAME: ")
    if response.upper() == "USERNAME":
        username()
    break

# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    numbers = list(range(100))
    for number in numbers:
        if number % 2 != 0:    
            print(number)
print(first_odds())

# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    a_list = [1, 5, 20]
    a_list.sort()
    print((a_list[-1]))
max_num_in_list(1)

# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
    return False
print(is_leap_year(2021))

# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    if len(a_list) == len(set(a_list)):
        return True
    else:
        return False
print(is_consecutive([1,2,3,4]))