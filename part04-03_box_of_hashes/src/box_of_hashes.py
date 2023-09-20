# Copy here code of line function from previous exercise
def line(number, string):
    star = "*"
    if string == "":
        print(f"{number*star}")
        return
    character = string[0]
    print(f"{number*character}")


def box_of_hashes(height):
    counter = 0
    while counter < height:
        line(10, "#")
        counter += 1

if __name__ == "__main__":
    box_of_hashes(5)
