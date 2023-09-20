# Write your solution here

def length_of_longest (my_list: list):
    first = my_list[0]
    best = len(first)
    for item in my_list:
        lenght = len(item)
        if lenght > best:
            best = len(item)
    return best

if __name__ == "__main__":
    my_list = ["car", "plane", "bus"]
    result = length_of_longest(my_list)
    print(result)

        