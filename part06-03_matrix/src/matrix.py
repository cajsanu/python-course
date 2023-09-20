# write your solution here
  
    
def matrix_max():
    with open("matrix.txt") as file:
        max = 0
        for line in file:
            numbers = line.split(",")
            for number in numbers:
                number = int(number)
                if number > max:
                    max = number
        return max
    
def row_sums():
    with open("matrix.txt") as file:
        sum_of_rows = []
        for line in file:
            row_sum = 0
            numbers = line.split(",")
            for number in numbers:
                number = int(number)
                row_sum += number
            sum_of_rows.append(row_sum)
        return sum_of_rows

def matrix_sum():
    with open("matrix.txt") as file:
        result = sum(row_sums())
        return result






if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())