#!/usr/bin/python3
def remove_char_at(str, n):
    res = ""
    for i in str:
        if i != str[n]:
            res += i
    return (res)
