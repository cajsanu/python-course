# Write your solution here
# You can test your function by calling it within the following block


def line(number, string):
    star = "*"
    if string == "":
        print(f"{number*star}")
        return
    character = string[0]
    print(f"{number*character}")



if __name__ == "__main__":
    line(10, "olq")



