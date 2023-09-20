# Write your solution here

import string
#print(dir(string))

def separate_characters(my_string: str):
    ascii_str = ""
    punct_str = ""
    rest = ""
    punct = string.punctuation
    ascii = string.ascii_letters
    for letter in my_string:
        if letter in ascii:
            ascii_str += letter
        elif letter in punct:
            punct_str += letter
        else:
            rest += letter
    
    return(ascii_str, punct_str, rest)


# parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
# print(parts[0])
# print(parts[1])
# print(parts[2])

    
