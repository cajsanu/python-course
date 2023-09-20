# Copy here code of line function from previous exercise

def line(number, string):
    star = "*"
    if string == "":
        print(f"{number*star}")
        return
    character = string[0]
    print(f"{number*character}")


def square_of_hashes(size):
    counter = 0
    while counter < size:
        line(size, "#")
        counter += 1
    


if __name__ == "__main__":
    square_of_hashes(5)
