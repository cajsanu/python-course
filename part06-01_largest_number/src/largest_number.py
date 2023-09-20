# write your solution here

def largest():
    with open("numbers.txt") as file:
        list = []
        for number in file:
            #number = number.replace("\n", "")
            number = int(number)
            list.append(number)
        largest_number = max(list)
        return largest_number
    


if __name__ == "__main__":
    print(largest())