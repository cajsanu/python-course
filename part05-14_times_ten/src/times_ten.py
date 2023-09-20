# Write your solution here


def times_ten(start_index: int, end_index: int):
    dict = {}
    for item in range(start_index,end_index+1):
        dict[item] = item*10
    return dict

    
    





if __name__ == "__main__":
    dict = times_ten(4,10)
    print(dict)