#!/usr/bin/env python3

#Function to reutn a list with every value from l1 and l2
def join_lists(l1, l2):
    temp_set = set(l1).union(set(l2)) #Convert to set variable to store it and remove duplicate values
    new_list = list(temp_set) #Convert set back to list
    return new_list #Return so converted list can be outputed when function is called in main code block

#Function to return a list that has matching values from list1 and list2    
def match_lists(l1, l2):
    temp_set = set(l1).intersection(set(l2)) #Convert list1 and list 2 to set to pull matching values
    new_list = list(temp_set) #Convert back to list so it can be outputted
    return new_list

#Function to reutrn different values between lists
def diff_lists(l1, l2):
    temp_set = set(l1).symmetric_difference(set(l2))
    new_list = list(temp_set)
    return new_list

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))