# Write your solution here


def create_tuple(x: int, y: int, z: int):
    list = [x, y, z]
    ordered = sorted(list)
    sum = x + y + z
    tuple = (ordered[0], ordered[2], sum )
    return tuple




if __name__ == "__main__":
    result = create_tuple(1,2,3)
    print(result)