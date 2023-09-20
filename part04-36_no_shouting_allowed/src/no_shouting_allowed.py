# Write your solution here

def no_shouting (my_list: list):
    new_list = []
    for item in my_list:
        if item.isupper():
            continue
        else:
            new_list.append(item)
    return new_list

if __name__ == "__main__":
    my_list = ["car", "PLANE", "bus"]
    result = no_shouting(my_list)
    print(result)

