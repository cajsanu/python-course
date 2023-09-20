




student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points = input("Exam points: ")
course_info = input("Course information: ")

# student_info = "students1.csv"
# exercise_data = "exercises1.csv"
# exam_points = "exam_points1.csv"
# course_info = "course1.txt"


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
    exercises_points = {}
    for line in file: 
        data = line.split(";")
        if data[0] == "id":
            continue
        exercises_completed[data[0]] = sum(map(int,data[1:]))
    
    max = 40
    for student in exercises_completed:
        if exercises_completed[student] < max*0.1:
            exercises_points[student] = 0
        elif max*0.1 <= exercises_completed[student] < max*0.2:
            exercises_points[student] = 1
        elif max*0.2 <= exercises_completed[student] < max*0.3:
            exercises_points[student] = 2
        elif max*0.3 <= exercises_completed[student] < max*0.4:
            exercises_points[student] = 3
        elif max*0.4 <= exercises_completed[student] < max*0.5:
            exercises_points[student] = 4
        elif max*0.5 <= exercises_completed[student] < max*0.6:
            exercises_points[student] = 5
        elif max*0.6 <= exercises_completed[student] < max*0.7:
            exercises_points[student] = 6
        elif max*0.7 <= exercises_completed[student] < max*0.8:
            exercises_points[student] = 7
        elif max*0.8 <= exercises_completed[student] < max*0.9:
            exercises_points[student] = 8
        elif max*0.9 <= exercises_completed[student] < max:
            exercises_points[student] = 9
        else: 
            exercises_points[student] = 10


with open(exam_points) as file: 
    exam_p = {}
    for line in file: 
        data = line.split(";")
        if data[0] == "id":
            continue
        exam_p[data[0]] = sum(map(int,data[1:]))
        
        

with open(course_info)as file, open("results.txt", "w") as txtfile, open("results.csv", "w") as csvfile:
    list =[]
    sign = "="
    for line in file:
        parts = line.strip() 
        parts = parts.split(":")
        parts[1] = parts[1].strip()
        list.append(parts)
    txtfile.write(f"{list[0][1]}, {list[1][1]} credits"+"\n")
    lenght = len(list[0][1]) + len(list[1][1]) + len(" , credits")
    txtfile.write(f"{lenght*sign}"+"\n")



    word = "name"
    txtfile.write(f"{word:30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}"+"\n")
    for person in students: 
        if person in exercises_completed and person in exam_p:
            summa = exercises_points[person] + exam_p[person]
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
            txtfile.write((f"{students[person]:30}{exercises_completed[person]:<10}{exercises_points[person]:<10}{exam_p[person]:<10}{summa:<10}{grade:<10}"+"\n"))
            
            csvfile.write(person+";")
            csvfile.write(students[person]+";")
            csvfile.write(str(grade)+"\n")
            
    
    


