# Write your solution here

def all_the_longest (my_list: list):
    list = []
    first = my_list[0]
    longest = first
    for item in my_list:
        lenght = len(item)
        if lenght >= len(longest):
            if lenght == len(longest):
                list.append(item)
                continue
            list.clear()
            list.append(item)
            longest = item
    return list
    

if __name__ == "__main__":
    my_list = ["car", "plane", "bullettrain", "automobile", "bike", "horsewaggon", "tram"]
    result = all_the_longest(my_list)
    print(result)