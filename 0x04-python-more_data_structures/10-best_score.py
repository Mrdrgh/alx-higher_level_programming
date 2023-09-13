#!/usr/bin/python3
def best_score(a_dictionary):
    l = list(a_dictionary)
    max = l[1] or None
    for i in l[1:]:
        if i > max:
            max = i
    return (max)
 