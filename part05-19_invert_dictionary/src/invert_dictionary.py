# Write your solution here

def invert(dictionary: dict):
    new_dictionary = {}
    for number, item in dictionary.items():
        new_dictionary[item] = number
    for item, number in new_dictionary.items():
        dictionary[item] = number
        del dictionary[number]
    
       
            

    
    


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
