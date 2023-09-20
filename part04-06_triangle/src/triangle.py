# Copy here code of line function from previous exercise
def line(number, string):
    star = "*"
    if string == "":
        print(f"{number*star}")
        return
    character = string[0]
    print(f"{number*character}")

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
    
if __name__ == "__main__":
    triangle(5)
