#!/usr/bin/python3
"""a misury to live, but the breathing continues"""


def text_indentation(text):
    """idk if it works , but bro i'm tired
    Args:
        text (str): a text bruh
    """
    if type(text) is not str:
        raise TypeError("text me be a string")
    for i in range(text):
        if text[i] is ".?:":
            print("", end="\n\n")
            while(text[i + 1] is " "):
                i += 1
        elif text[i] is " ":
            j = i
            while text[i] is " ":
                i += 1
                if text[i] is not " .?:":
                    i = j
                    break
        print("{:c}".format(text(i)), end="")
            