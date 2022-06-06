#!/usr/bin/python3
def no_c(my_string):
   j,  new_string = 0,  my_string[:]

    for i in range(len(my_string)):
        if (my_string[i] == 'c' or my_strint[i] == 'C'):
            new_string = new_string[:(i-j)] + my_string[(i + 1):]
            j += 1
    return new_string
