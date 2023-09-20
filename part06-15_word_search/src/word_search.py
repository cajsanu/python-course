# Write your solution here

# if A or B === if !A and !B
# if A and B === if !A or !B


def find_words(search_term: str):
    list_of_words = []
    asterisk = "*"
    with open("words.txt") as file:
        for line in file: 
            line = line.strip()
            if line == search_term:
                list_of_words.append(line)
                continue
            if search_term[0] == asterisk:
                if line.endswith(search_term[1:]):
                    list_of_words.append(line)
            if search_term[-1] == asterisk:
                if line.startswith(search_term[0:len(search_term)-1]):
                    list_of_words.append(line)
            if len(line) == len(search_term):
                index = 0
                for letter in search_term:
                    if letter == "." or letter == line[index]:
                        index += 1
                        if index == len(line):
                            list_of_words.append(line)
                    else:
                        break

                

    return list_of_words



# result = find_words("ca.")
# print(result)