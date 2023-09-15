#!/usr/bin/python3
def best_score(a_dictionary):
    l = list(a_dictionary)
    max = l[1]
    for i in l:
        if i > max:
            max = i
    return (max)
 