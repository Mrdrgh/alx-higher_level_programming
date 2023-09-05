#!/usr/bin/python3
def remove_char_at(str, n):
    res = ""
    if len(str) <= n or n < 0:
        return (str)
    for i in str:
        if i != str[n]:
            res += i
    return (res)
