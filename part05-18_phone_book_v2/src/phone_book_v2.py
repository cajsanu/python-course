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
        for value in dictionary[name]:
            print(value)
    else:
        print("no number")
    

def add (dictionary: dict):
    nr_list = []
    name = input("name: ")
    number = input("number: ")
    print("ok!")
    if name not in dictionary:
       dictionary[name] = []
    dictionary[name].append(number)
        

phone_book()