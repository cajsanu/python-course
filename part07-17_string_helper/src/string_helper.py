# Write your solution here
        


def change_case(orig_string: str):
    from string import ascii_lowercase, ascii_uppercase
    lower = ascii_lowercase
    upper = ascii_uppercase
    new_string = ""
    for letter in orig_string:
        if letter in lower:
            new_string += letter.upper()
        elif letter in upper:
            new_string += letter.lower()
        else: 
            new_string += letter
    return new_string


def split_in_half(orig_string: str):
    half_way = len(orig_string) // 2
    return (orig_string[:half_way], orig_string[half_way:])


def remove_special_characters(orig_string: str):
    from string import ascii_letters, digits
    new_string = ""
    for letter in orig_string:
        if letter in ascii_letters or letter in digits or letter == " ":
            new_string += letter
        else: 
            continue     
    return new_string
            
            

            
    