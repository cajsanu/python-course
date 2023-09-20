# write your solution here

def read_fruits():
    with open("fruits.csv") as file:
        dict = {}
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(";")
            number = float(parts[1])
            dict[parts[0]] = number
        return dict





if __name__ == "__main__":
    print(read_fruits())