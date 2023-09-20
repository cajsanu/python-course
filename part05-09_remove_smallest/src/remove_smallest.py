# Write your solution here

def remove_smallest (numbers: list):
    new_list = numbers[:]
    smallest = sorted(new_list)[0]
    numbers.remove(smallest)



