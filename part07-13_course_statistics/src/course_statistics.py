# Write your solution here


import urllib.request
import json

def retrieve_all():
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    request = urllib.request.urlopen(address)
    data = json.loads(request.read())
    list_of_exercises = []
    for week in data: 
        if week["enabled"] == True:
            summa = sum(week["exercises"])
            list_of_exercises.append((week["fullName"], week["name"], week["year"], summa))
    return list_of_exercises



def retrieve_course(course_name: str):
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    address = url + "/" + course_name + "/stats"
    request = urllib.request.urlopen(address)
    data = json.loads(request.read())
    index = 0
    sum_of_hours = 0
    sum_of_exercises = 0
    max_amount_of_students = 0
    while index <= len(data):
        if str(index) not in data:
            index += 1
            continue
        sum_of_hours += data[str(index)]["hour_total"]
        sum_of_exercises += data[str(index)]["exercise_total"]
        index += 1
    for week in data:
        if data[week]["students"] > max_amount_of_students:
            max_amount_of_students = data[week]["students"]
    exer_av = sum_of_exercises // max_amount_of_students
    hours_av = sum_of_hours // max_amount_of_students
    
    return {"weeks":len(data), "students":max_amount_of_students, "hours":sum_of_hours, "hours_average": hours_av, "exercises":sum_of_exercises, "exercises_average": exer_av}
        
        
    
    
    
    
# retrieve_course("CCFUN")
# retrieve_all()
