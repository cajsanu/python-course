# Write your solution here


def phone_book ():
    dictionary = {}
    while True:
        number = int(input("command (1 search, 2 add, 3 quit):"))
        if number >= 3:
            print("quitting...")
            break
        elif number == 2:
            add(dictionary)
        elif number == 1:
            search(dictionary)
        

def search (dictionary: dict):
    name = input("name: ")
    if name in dictionary:
        print(dictionary[name])
    else:
        print("no number")
    

def add (dictionary: dict):
    name = input("name: ")
    number = input("number: ")
    print("ok!")
    dictionary[name] = number
        

phone_book()




