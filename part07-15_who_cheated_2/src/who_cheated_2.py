# Write your solution here

from datetime import date, datetime, time, timedelta

def final_points():
    points = {}
    students = get_submission_data("submissions.csv")
    for name in students:
        for task_nr in students[name]: 
            p = students[name][task_nr]["points"] 
            if name in points:   
                points[name] += p  
            else: 
                points[name] = p 
    return points

    


def get_start_time(data:str):
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




def get_submission_data(data:str):
    with open(data) as file:
        start_times = get_start_time("start_times.csv")
        names_and_tasks = {}
        limit = timedelta(hours=3)
        for line in file:
            line = line.strip()
            parts = line.split(";")
            name = parts[0]
            task = int(parts[1])
            points = int(parts[2])
            times = parts[-1].split(":")
            times = time(int(times[0]), int(times[1]))
            submission_time = datetime.combine(date.today(), times)
        
            if name in names_and_tasks:
                if task in names_and_tasks[name]:
                    if points > names_and_tasks[name][task]['points'] and start_times[name] + limit > submission_time:
                        names_and_tasks[name][task] = { 'points': points, 'times': submission_time }
                else:
                    names_and_tasks[name][task] = { 'points': points, 'times': submission_time }
            else: 
                names_and_tasks[name] = {}
                names_and_tasks[name][task] = { 'points': points, 'times': submission_time }
    return names_and_tasks
    
        


# print(final_points())