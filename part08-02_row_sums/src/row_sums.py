# Write your solution here


def row_sums(my_matrix: list):
    for list in my_matrix:
        summa = sum(list)
        list.append(summa)
    
    
    
# my_matrix = [[1, 2], [3, 4]]
# row_sums(my_matrix)
# print(my_matrix)