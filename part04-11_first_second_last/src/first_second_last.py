# Write your solution here

def first_word (string):
    first = string.find(" ")
    word = string[0:first]
    return word

def second_word (string):
    first = string.find(" ")
    second = string.find(" ", first+1)
    if second == -1:
        word = string[first+1:]
    else:
        word = string[first+1:second]
    return word

def last_word (string):
    last = string.rfind(" ")
    word = string[last+1:]
    return word

if __name__ == "__main__":
    sentence = "once upon"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))