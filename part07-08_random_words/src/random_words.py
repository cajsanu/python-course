# Write your solution here

import random

def words(n: int, beginning: str):
    with open("words.txt") as file: 
        match = []
        for line in file: 
            line = line.strip()
            if line.startswith(beginning):
                match.append(line)
        if len(match) < n:
            raise ValueError
        else:
            words = random.sample(match, n)
            return words



# word_list = words(9, "aa")
# for word in word_list:
#     print(word)

        


