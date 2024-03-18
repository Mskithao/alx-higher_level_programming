#!/usr/bin/python3
#above is a shebang, indicating the path to the python interpretor

#prototype: function defination - 'print_list_interger' taking 1 argument'my_list' initialized with an empty list by default
def print_list_integer(my_list=[]):

    #iterate through each element in 'my_list'.
    for num in my_list:
        #print each interger element from 'my_list' using string formating to ensure it is printed as an integer
        print("{:d}".format(num))
