# Copy here code of line function from previous exercise

def line(number, string):
    star = "*"
    if string == "":
        print(f"{number*star}")
        return
    index = string[0]
    print(f"{number*index}")

def square(size, character):
    counter = 0
    while counter < size:
        line(size, character)
        counter += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(20, "+")