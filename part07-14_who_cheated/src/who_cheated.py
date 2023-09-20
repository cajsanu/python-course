# Write your solution here


from datetime import date, datetime, time, timedelta

def cheaters():
    start_time = get_time("start_times.csv")
    end_time = get_time("submissions.csv")
    limit = timedelta(hours=3)
    list = []
    for person in start_time:
        for name in end_time:
            if name == person:
                if start_time[person] + limit < end_time[name]:
                    list.append(name)
    return list
       
            

def get_time(data:str):
    with open(data) as file:
        names_and_times = {}
        for line in file:
            line = line.strip()
            parts = line.split(";")
            times = parts[-1].split(":")
            times = time(int(times[0]), int(times[1]))
            times = datetime.combine(date.today(), times)
            if parts[0] in names_and_times:
                if times > names_and_times[parts[0]]:
                    names_and_times[parts[0]] = times
            else: 
                names_and_times[parts[0]] = times
    return names_and_times
        



# cheaters()
# get_time("start_times.csv")