#!/usr/bin/env python3
import lab4b

#Dictionaries
dict_york = {'Address': '70 The Pond Road', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}

#Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

#Function to combine list_keys and list_values into a dictionary using while loops
def create_dictionary(keys, values):
    temp_dict = {}
    i = 0 #Counter to keep track of where we are in index
    while i < len(keys) and i < len(values): #While at index number i if the amount of items in the lists keys and values (len) is less than the index
        temp_dict[keys[i]] = values[i] #Add the item at the index number key list and value list into dictionary list as a key value pair
        i = i + 1 #Increase the index counter to move onto the next list item
    return temp_dict

#Function to find all shared values between two dictionary lists passed to the function and return results as set
def shared_values(dict1, dict2):
    combined_set = set(dict1.values()).intersection(set(dict2.values())) #Convert the values in dict1 and dict 2 into sets and intersect them to create one set list
    return combined_set

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)
