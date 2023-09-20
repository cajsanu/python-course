# Write your solution here

list = []
counter = 1

while True:
    print(f"The list is now {list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")

    if choice == "d":
        list.append(counter)
    elif choice == "r":
        list.pop(-1)
        counter -= 2
    elif choice == "x":
        print("Bye!")
        break
    counter += 1
    
    