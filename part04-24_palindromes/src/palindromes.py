# Write your solution here


#MY FAILED ATTEMPT AT SOLVING
#def palindromes (word: str):
    #while True:
        #word = input("Please type in a palindrome: ")
        #halfway = len(word)//2
        #first_half = sorted(word[:halfway])
        #second_half = sorted(word[halfway:], reverse=True)
        #first_half = first_half.lower()
        #second_half = second_half.lower()
        #if first_half == second_half:
            #print(f"{word} is a palindrome!")
        #else:
            #print(f"{word} wasn't a palindrome")

def palindromes (word: str):
    if word == word[::-1]:   #this is done to check if the word is the same from front to back and back to front
        return True
    else:
        return False


def main_function ():
     while True:
        word = input("Please type in a palindrome: ").lower()
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        else:
            print(f"that wasn't a palindrome")

main_function()
    


# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
