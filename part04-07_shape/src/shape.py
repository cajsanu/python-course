# Copy here code of line function from previous exercise and use it in your solution

def line(number, string):
    star = "*"
    if string == "":
        print(f"{number*star}")
        return
    index = string[0]
    print(f"{number*index}")

def triangle(size):
    counter = 1
    while counter <= size:
        line(counter, "#")
        counter += 1

def square(size, character):
    counter = 0
    while counter < size:
        line(size, character)
        counter += 1

def shape (size, character, row, character2):
    counter = 1
    while counter <= size:
        line(counter, character)
        counter += 1
    counter = 1
    while counter <= row:
        line(size, character2)
        counter += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")