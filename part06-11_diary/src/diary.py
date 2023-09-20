# Write your solution here

while True: 
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Funktion: "))
    if function == 0:
        print("Bye now!")
        break

    if function == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as file:
            file.write(entry + "\n")
        print("Diary saved")

    if function == 2:
        print("Entries")
        with open("diary.txt") as file: 
            contents = file.read()
            print(contents)



