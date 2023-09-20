# Write your solution here


def filter_incorrect():
    with open("lottery_numbers.csv") as file,  open("correct_numbers.csv", "w") as corrects:
        for line in file: 
            dict = {}
            row = line.strip()
            row = row.split(";")
            dict[row[0]] = row[1]
            items = []
            index = 1
            for k, v in dict.items():
                k = k.split(" ")
                v = v.split(",")
                try:
                    if int(k[1]) not in range(1,52):
                        break
                except ValueError:
                    break
                if len(v) != 7:
                    break
                for number in v:
                    try:
                        if int(number) < 39 and int(number) >= 1 and number not in items:
                            index += 1
                            if index == 7:
                                corrects.write(line)
                        else:
                            break
                    except ValueError:
                        break
                    items.append(number)
                            
                    

if __name__ == "__main__":

    filter_incorrect()