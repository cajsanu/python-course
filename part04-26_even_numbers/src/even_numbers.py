# Write your solution here

def even_numbers(lst:list):
    list = []
    for item in lst:
        if item % 2 == 0:
            list.append(item)
    return list


if __name__ == "__main__":
    my_list = [12, 21, 3, 44, 56]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)  
            


