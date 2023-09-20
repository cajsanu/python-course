# Write your solution here


def range_of_list (items: list):
   return max(items) - min(items)

if __name__ == "__main__":
    my_list = [5, 2, 4]
    result = range_of_list(my_list)
    print(result)