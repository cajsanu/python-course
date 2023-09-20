# Write your solution here


def histogram (word: str):
    dict = {}
    for letter in word:
        if letter not in dict:
            dict[letter] = 0*"*"
        dict[letter] += 1*"*"
    for key, value in dict.items():
        print(key,value)



if __name__ == "__main__":
    result = histogram("abba")
    
