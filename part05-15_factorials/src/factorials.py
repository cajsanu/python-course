# Write your solution here


def factorials(n: int):
    dict = {} 
    for item in range(1,n+1):
        if item == 1:
            dict[item] = 1
            continue
        dict[item] = item * dict[item-1]
    return dict





if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])