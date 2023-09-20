# Write your solution here

def double_items (numbers: list):
    new_list = []
    for number in numbers:
        new_list.append(number*2)
    return new_list
    
if __name__ == "__main__":
    my_list = [1,2,3,4,5]
    print(double_items(my_list))
    print(my_list)