#!/usr/bin/env python3
def no_c(my_string):
    new_string = ''
    for i in my_string:
        if(i != 'c') and (i != 'C'):
            new_string += i

    new_str = new_string
    return new_str

