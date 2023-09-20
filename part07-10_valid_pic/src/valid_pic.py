# Write your solution here

from datetime import datetime


def is_it_valid(pic: str):
    century_mark = pic[6]
    control_character = pic[-1]
    if century_mark == "-":
        year = "19" + pic[4:6]
    elif century_mark == "+":
        year = "18" + pic[4:6]
    else:
        year = "20" + pic[4:6]
    cc = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    try: 
        date = datetime(int(year), int(pic[2:4]), int(pic[0:2]))
        if century_mark == "+" or century_mark == "-" or century_mark == "A":
            number = int(pic[0:6]+ pic[7:10])  % 31
            if control_character == cc[number]:
                if len(pic) == 11:
                    return True
    except ValueError:
        pass
    return False
    

#result = is_it_valid("030103A493DD")




