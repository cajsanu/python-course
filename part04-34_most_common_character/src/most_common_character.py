# Write your solution here

def most_common_character (my_string: str):
    first = my_string[0]
    most_common = first
    for character in my_string:
        if my_string.count(character) >= my_string.count(most_common):
            most_common = character
    return most_common
        
 
        

if __name__ == "__main__":
    my_string = "aab"
    result = most_common_character(my_string)
    print(result)