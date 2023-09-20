# Write your solution here


def longest_series_of_neighbours (my_list: list):
    first = my_list[0]
    item = first
    counter = 1
    index = 0
    longest = 0
    for number in my_list:
        if item + 1 == number or item -1 == number:
            counter += 1
            if counter > longest:
                longest = counter
        else: 
            counter = 1
        item = my_list[index]
        index += 1
    return longest

if __name__ == "__main__":
    my_list = [1,2,3,5,7,6,5,4,5]
    result = longest_series_of_neighbours(my_list)
    print(result)


