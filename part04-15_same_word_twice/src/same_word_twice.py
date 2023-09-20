# Write your solution here

list = []

while True:
    words = input("Word: ")
    if words in list:
        break
    list.append(words)
    count = len(list)
print(f"You typed in {count} different words")
