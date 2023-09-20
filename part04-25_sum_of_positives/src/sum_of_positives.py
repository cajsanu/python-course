# Write your solution here


def sum_of_positives (lst: list):
    sum = 0
    for item in lst:
        if item > 0:
            sum += item
    return sum


if __name__ == "__main__":
    my_list = [4, -44, 4, -4, 4]
    result = sum_of_positives(my_list)
    print("The result is", result)