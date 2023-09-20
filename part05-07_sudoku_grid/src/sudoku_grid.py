# Write your solution here

def sudoku_grid_correct (sudoku: list):
        row_no = 0
        col_no = 0
        row_i = 0
        col_i = 0
        while row_no <= 8:
            if column_correct(sudoku, col_no) == True:
                 col_no += 1
            else:
                return False

            if row_correct(sudoku, row_no) == True:
                row_no += 1
            else:
                 return False
            
        while row_i <= 6:
            col_i = 0
            while col_i <= 6:
                if block_correct(sudoku, row_i, col_i) == True:
                    col_i += 3
                else: 
                    return False
            row_i += 3
        return True         
                    

def column_correct (sudoku: list, column_no: int):
    list = []
    for row in sudoku:
        item = row[column_no]
        if item > 0 and item in list:
            return False
        list.append(item)
    return True

def row_correct (sudoku: list, row_no: int):
    list = []
    for item in sudoku[row_no]:
            if item > 0 and item in list:
                return False
            list.append(item)
    return True

def block_correct (sudoku: list, row_no: int, column_no: int):
    list = []
    
    for row in sudoku[row_no:row_no + 3]:
        for item in row[column_no:column_no + 3]:
            if item > 0 and item in list:
                return False
            list.append(item)         
    return True


if __name__ == "__main__":
    sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku1))
    print(sudoku_grid_correct(sudoku2))
    