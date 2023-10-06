# WRITE YOUR SOLUTION HERE:

import string

def most_common_words(filename: str, lower_limit: int):
    with open(filename) as file: 
        file = file.read()
        file = file.strip()
        exclude = set(string.punctuation)
        file = ''.join(character for character in file if character not in exclude)
        file = file.split()
        
        return {word: file.count(word) for word in file if file.count(word) >= lower_limit}
        
    
    
words = most_common_words("comprehensions.txt", 3)
print(words)