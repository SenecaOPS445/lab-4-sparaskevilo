#!/usr/bin/env python3


#Function that has every value from s1 and s2
def join_sets(s1, s2):
    return s1 | s2 #Return union of s1 and s2 so it can be display with print
    

#Function that will reutrn matching values in s1 and s2
def match_sets(s1, s2):
    return s1 & s2 #Return matching values
    

#Function that returns the different values in s1 and s2
def diff_sets(s1, s2):
    return s1 ^ s2

#Main code block
if __name__ == '__main__':
    set1 = set(range(1,10))
    set2 = set(range(5,15))
    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))