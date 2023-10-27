# Write your solution here
import re


def is_dotw(my_string: str):
    if re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string):
        return True
    return False

def all_vowels(my_string: str):
    if re.search("^[aeiou$]*$", my_string):
        return True
    return False

def time_of_day(my_string: str):
    if re.search("^([0-2][0-4]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])$", my_string):
        return True
    return False


# print(time_of_day("23:05:00"))
# print(time_of_day("AB:01:CD"))
# print(time_of_day("23:59:59"))
# print(time_of_day("33:66:x7"))