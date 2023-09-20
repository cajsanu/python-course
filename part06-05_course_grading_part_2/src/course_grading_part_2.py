# wwite your solution here


student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")



with open(student_info) as file:
    students = {}
    for line in file: 
        line = line.strip()
        student = line.split(";")
        if student[0] == "id":
                continue 
        students[student[0]] = student[1] + " " + student[2]
    

with open(exercise_data) as file: 
    exercises_completed = {}
    for line in file: 
        data = line.split(";")
        if data[0] == "id":
            continue
        exercises_completed[data[0]] = sum(map(int,data[1:]))
    max = 40

    for student in exercises_completed:
        if exercises_completed[student] < max*0.1:
            exercises_completed[student] = 0
        elif max*0.1 <= exercises_completed[student] < max*0.2:
            exercises_completed[student] = 1
        elif max*0.2 <= exercises_completed[student] < max*0.3:
            exercises_completed[student] = 2
        elif max*0.3 <= exercises_completed[student] < max*0.4:
            exercises_completed[student] = 3
        elif max*0.4 <= exercises_completed[student] < max*0.5:
            exercises_completed[student] = 4
        elif max*0.5 <= exercises_completed[student] < max*0.6:
            exercises_completed[student] = 5
        elif max*0.6 <= exercises_completed[student] < max*0.7:
            exercises_completed[student] = 6
        elif max*0.7 <= exercises_completed[student] < max*0.8:
            exercises_completed[student] = 7
        elif max*0.8 <= exercises_completed[student] < max*0.9:
            exercises_completed[student] = 8
        elif max*0.9 <= exercises_completed[student] < max:
            exercises_completed[student] = 9
        else: 
            exercises_completed[student] = 10
        


with open(exam_points) as file: 
    exam_p = {}
    for line in file: 
        data = line.split(";")
        if data[0] == "id":
            continue
        exam_p[data[0]] = sum(map(int,data[1:]))
        

for person in students: 
    if person in exercises_completed and person in exam_p:
        summa = exercises_completed[person] + exam_p[person]
        if summa <= 14:
            grade = 0
        elif 15 <= summa <= 17:
            grade = 1
        elif 18 <= summa <= 20:
            grade = 2
        elif 21 <= summa <= 23:
            grade = 3
        elif 24 <= summa <= 27:
            grade = 4
        else: 
            grade = 5
        print(f"{students[person]} {grade}")

