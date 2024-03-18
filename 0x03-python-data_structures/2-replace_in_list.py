#!/usr/bin/python3

#function replace_in_list taking 3 arags
#my list is the lsit to modify
#idx the index where the list will be modify
#element: the new element to be inserted in the specified index
def replace_in_list(my_list, idx, element):

    #checks if idx is 0 or out of range and returns the original list
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    #if index is within range of the list the lement at specified index is replaced
    #returns the modified list
    else:
        my_list[idx] = element
        return my_list
