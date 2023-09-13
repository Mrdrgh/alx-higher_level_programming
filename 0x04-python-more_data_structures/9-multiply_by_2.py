#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary
    for i in new_dic.values():
        i **= 2
    return (new_dic)
