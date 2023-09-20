# Write your solution here

def shortest (my_list: list):
    first = my_list[0]
    best = first
    for item in my_list:
        lenght = len(item)
        if lenght < len(best):
            best = item
    return best 

if __name__ == "__main__":
    my_list = ["bus", "plane", "bike"]
    result = shortest(my_list)
    print(result)