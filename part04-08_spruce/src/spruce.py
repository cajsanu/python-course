# Write your solution here

def spruce (size):
    print("a spruce!")
    character = "*"
    white_space = " "
    counter = 1
    lenght = size
    while counter <= size:
        print(f"{(lenght-1)*white_space+character}")
        counter += 1
        character += "**"
        lenght -= 1
    character = "*"
    print(f"{(size-1)*white_space+character}")  
        


if __name__ == "__main__":
    spruce(8)