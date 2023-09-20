# Write your solution here




def list_of_stars(my_list: list):
    counter = 0
    star = "*"
    while counter < len(my_list):
        item = my_list[counter]
        print(f"{item*star}")
        counter += 1
    

if __name__ == "__main__":
    my_list = [10, 6, 4, 1, 8, 33]
    list_of_stars(my_list)
    

