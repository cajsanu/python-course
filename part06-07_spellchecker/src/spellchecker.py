# write your solution here


with open("kaikkisanat.txt") as file:
    text = input("Write text: ")
    text = text.split()
    list_of_words = []
    for items in file:
        list_of_words.append(items.strip())
    for word in text: 
        if word.lower() in list_of_words: 
            print(word + " ", end="")
        else: 
            word = (f"*{word}*")
            print(word + " ", end="")
    print()

        
                
           
       
    
        
            
    
    
