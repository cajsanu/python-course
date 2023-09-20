# Write your solution here


def transpose(matrix: list):
    new_matrix = []
    new_list = []
    col_no = 0 
    index = 0
    while col_no < len(matrix):
        for row in matrix:
            number = row[col_no]
            new_list.append(number)
        col_no += 1
        new_matrix.append(new_list)
        new_list = []
    for item in range(len(matrix)):
        matrix[item] = new_matrix[index]
        index += 1



if __name__ == "__main__":
    matrix = [[1,2],[1,2]]
    transpose(matrix)
    print(matrix)