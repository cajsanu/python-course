# Write your solution here


def dictionary(): 
    while True: 
        print("1 - Add word, 2 - Search, 3 - Quit")
        user_input = int(input("Function: "))
        if user_input == 1:
            with open("dictionary.txt", "a") as file: 
                f = input("The word in Finnish: ")
                e = input("The word in English: ")
                print("Dictionary entry added")
                file.write(f"{f};{e}""\n")
        if user_input == 2:
            with open("dictionary.txt") as file:
                word = input("Search term: ")
                for line in file:
                    line = line.strip()
                    line = line.split(";")
                    if word in line[0] or word in line[1]:
                        print(f"{line[0]} - {line[1]}")
        if user_input == 3:
            print("Bye!")
            break
        

    

dictionary()
        
