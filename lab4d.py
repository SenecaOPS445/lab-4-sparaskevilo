#!/usr/bin/env python3

#String variables
str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

#Function that returns first five characters of string argument
def first_five(string):
    First5 = string[0:5]
    return First5

#Returns last seven characters
def last_seven(string):
    Last7 = string[-7:]
    return Last7

#Accepts integer and returns second and third characters
def middle_number(number):
    Two_Three = str(number)[1:3]
    return Two_Three

#Function that concatenates the first three characters of argument 1 and last three characters of argument2
def first_three_last_three(string1, string2):
    combo_string = string1[0:3] + string2[-3:]
    return combo_string



if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))