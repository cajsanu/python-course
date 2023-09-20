# Write your solution here

from difflib import get_close_matches

with open("wordlist.txt") as file:
    text = input("Write text: ")
    text = text.split()
    list_of_words = []
    list_of_miss_spellt = []
    for items in file:
        list_of_words.append(items.strip())
    for word in text: 
        if word.lower() in list_of_words: 
            print(word + " ", end="")
        else: 
            miss_spellt_word = word
            print(f"*{word}* ", end="")
            list_of_miss_spellt.append(miss_spellt_word)
    print()      
    print("suggestions: ")
            
    for i in list_of_miss_spellt: 
        matching = get_close_matches(i, list_of_words)
        print(f"{i}: {matching[0]}, {matching[1]}, {matching[2]}")
       
    
    

    

