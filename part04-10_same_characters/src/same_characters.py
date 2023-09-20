# Write your solution here


def same_chars (string, index1, index2):
    if index1 >= len(string) or index2 >= len(string):
        return False
    first = string[index1]
    second = string[index2]
    if first == second:
        return True
    else:
        return False
    

if __name__ == "__main__":
    print(same_chars("abc", 0, 3))