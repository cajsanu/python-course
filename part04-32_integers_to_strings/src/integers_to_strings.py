# Write your solution here

def formatted (my_list: list):
    formatted_list = []
    for number in my_list:
        number = f"{number:.2f}"
        formatted_list.append(number)
    return formatted_list

if __name__ == "__main__":
    my_list = [2.5555, 89.056, 3.456]
    result = formatted (my_list)
    print(result)