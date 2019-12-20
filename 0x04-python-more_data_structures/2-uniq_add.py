#!/usr/bin/python3
def uniq_add(my_list=[]):
    addition = 0
    for i in set(my_list):
        addition += i
    return addition
