# Write your solution here


def print_sudoku (sudoku: list):
    for row in range(len(sudoku)):
        print()
        if row % 3 == 0 and row != 0:
             print()
        for item in range(len(sudoku[row])):
            if item % 3 == 0 and item != 0:
                 print(" ", end="")

            if sudoku[row][item] == 0:
                print("_ ", end="")
            else:
                print(sudoku[row][item], end=" ")
    print()

def copy_and_add (sudoku: list, row_no: int, column_no: int, number: int):
    new_list = []
    for row in sudoku:
        new_list.append(row[:])
    new_list[row_no][column_no] = number
    return new_list
        
     

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)


