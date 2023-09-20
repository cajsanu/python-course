# Write your solution here

def anagrams (word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
    
if __name__ == "__main__":
    word1 = "xyZ"
    word2 = "yXz"
    result = anagrams(word1, word2)
    print(result)