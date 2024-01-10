#!/usr/bin/python3
def uniq_add(my_list=[]):
     unique_set = set(my_list)
     for num in my_list:
         result = sum(unique_set)
         return result
