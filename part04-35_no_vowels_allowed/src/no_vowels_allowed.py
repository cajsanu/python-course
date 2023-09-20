# Write your solution here

def no_vowels (my_string: str):
    new_string = ""
    for letter in my_string:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            continue
        else:
            new_string = new_string + letter
    return new_string

if __name__ == "__main__":
    my_string = "hey there"
    result = no_vowels(my_string)
    print(result)

