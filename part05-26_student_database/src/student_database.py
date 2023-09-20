# Write your solution here

def add_student(database: dict, name: str):
    database[name] = []


def print_student(database: dict, name: str):
    if name not in database:
        print(f"{name}: no such person in the database")
    elif name in database:
        print(name+":")
        if len(database[name]) == 0:
            print(" no completed courses")
        else: 
            print(f" {len(database[name])} completed courses:")
            for saved_course in database[name]:
                print("  " + saved_course[0], saved_course[1])
            average_grade( database, name)


def add_course (database: dict, name: str, course_and_grade: tuple): 
    if name in database:
        counter = 0
        if course_and_grade[1] == 0:
                return
        for saved_course in database[name]: 
            if course_and_grade[0] in saved_course and course_and_grade[1] >= saved_course[1]:
                database[name][counter] = course_and_grade
                return
            if course_and_grade[0] in saved_course and course_and_grade[1] < saved_course[1]:
                return
            counter += 1

        database[name].append(course_and_grade)


def average_grade (database: dict, name: str):
    av_grade = 0
    if name in database:
        for courses in database[name]:
            av_grade += courses[1]
    print(f" average grade {av_grade/len(database[name])}")


def summary (database: dict):
    print(f" students {len(database)}")
    most_courses = 0
    av_grade = 0
    best_grade = 0
    for student in database:
        if len(database[student]) == 0:
            continue
        grades = 0
        if len(database[student]) > most_courses:
            most_courses = len(database[student])
            name = student
        for courses in database[student]:
            grades += courses[1]
        av_grade = grades/len(database[student])
        if av_grade > best_grade:
            best_grade = av_grade
            person = student
    
    print(f"most courses completed {most_courses} {name}") 
    print(f"best average grade {best_grade} {person}")


        
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_student(students, "Severus")
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 4))
    add_course(students, "Peter", ("Advanced Course in Programming", 3))
    add_course(students, "Peter", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    average_grade(students, "Peter")
    print_student(students, "Peter")
    print_student(students, "Severus")
    summary(students)    


