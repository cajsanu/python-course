# Write your solution here

def count_matching_elements (my_matrix: list, element: int):
    counter = 0
    for list in my_matrix:
        for item in list:
            if item == element:
                counter += 1
    return counter

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 2, 4, 5, 3, 4], [1, 0, 0, 0]]
    print(count_matching_elements(m, 4))

