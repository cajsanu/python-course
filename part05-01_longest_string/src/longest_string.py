# Write your solution here

def longest (strings: list):
    first = strings[0]
    longest_string = first
    for str in strings:
        if len(str) > len(longest_string):
            longest_string = str
    return longest_string


if __name__ == "__main__":
    my_string = ["Hi", "How", "You", "Doing"]
    result = longest(my_string)
    print(result)
