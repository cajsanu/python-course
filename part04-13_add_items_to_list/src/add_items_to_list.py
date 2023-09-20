# Write your solution here

list = []
items = int(input("How many intems: "))
counter = 1

while counter <= items:
    item = int(input(f"Item {counter}: "))
    list.append(item)
    counter += 1

print(list)