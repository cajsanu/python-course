# write your solution here



student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")



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
        exercises_completed[data[0]] = map(int,data[1:])
       
        

for person in students: 
    if person in exercises_completed:
        print(f"{students[person]} {sum(exercises_completed[person])}")
        
        
                


       

   
          

