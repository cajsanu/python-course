class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade
        
    def get_student_name(self):
        return self.student_name

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
    
    
def accepted(attempts: list):
    return list(filter(lambda accepted : accepted.grade >= 1, attempts))


def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda attempt : attempt.grade == grade, attempts))


def passed_students(attempts: list, course: str):
    students = list(filter(lambda student : student.course_name == course and student.grade >= 1, attempts))
    return sorted(map(lambda s : s.get_student_name(), students))
    



# s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
# s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
# s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
# s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

# for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
#     print(attempt)


