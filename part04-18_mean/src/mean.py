# Write your solution here


def mean (items: list):
    summa = sum(items)
    count = len(items)
    return summa/count

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(f"mean value is {result}")