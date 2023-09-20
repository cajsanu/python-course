# Write your solution here

from datetime import datetime, timedelta

document = input("Filename: ") 
start_date = input("Starting date: ") 
number_of_days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile): ") 


date = datetime.strptime(start_date, "%d.%m.%Y")
start = datetime.strptime(start_date, "%d.%m.%Y")
day = timedelta(days=1)
summa = 0
dic_of_sctm = {}
for i in range(number_of_days):
    sctm = input(f"Screen time {date.strftime('%d.%m.%Y')}: ")
    parts = sctm.split()
    list = []
    for part in parts:
        p = int(part)
        list.append(p)
        dic_of_sctm[date.strftime('%d.%m.%Y')] = list
    date += day
    summa += sum(list)
average = summa / number_of_days
date -= day

with open(document, "w") as file:
    file.write(f"Time period: {start.strftime('%d.%m.%Y')}-{date.strftime('%d.%m.%Y')}\n")
    file.write(f"Total minutes: {summa}\n")
    file.write(f"Average minutes: {average}\n")
    for k, v in dic_of_sctm.items():
        file.write(k)
        file.write(f": {v[0]}/{v[1]}/{v[2]}\n")


print(f"Data stored in file {document}")


