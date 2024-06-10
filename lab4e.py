#!/usr/bin/env python3
#Author ID: sparaskevilo

#Define numbers to compare with list items
integers = '0123456789'

#Takes string and reutrns true if all the characters in the string are digits and false if they are not
#Use countdown and length to traverse list and keep track of index
def is_digits(sobj):
    counter = 0
    while counter < len(sobj):
        for item in sobj: #Loop through each character
            if item in integers:
                counter = counter + 1
            else:
                return False
    return True

                   
if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')