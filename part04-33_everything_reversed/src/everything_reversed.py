# Write your solution here


def everything_reversed (my_list: list):
    new_list = []
    for item in my_list:
        item = item[::-1]
        new_list.append(item)
    return new_list[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "hello", "bye"]
    result = everything_reversed(my_list)
    print(result)
