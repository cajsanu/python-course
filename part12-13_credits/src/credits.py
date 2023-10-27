from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

from functools import reduce

def sum_of_all_credits(attempts: list):
    return reduce(lambda credits, attempt : credits + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    grade_passed = filter(lambda attempt : attempt.grade >= 1, attempts)
    return reduce(lambda cred_sum, attempt : cred_sum + attempt.credits, grade_passed, 0)

def average(attempts: list):
    grade_passed = list(filter(lambda attempt : attempt.grade >= 1, attempts))
    return (reduce(lambda grade_sum, attempt : grade_sum + attempt.grade, grade_passed, 0)) / len(grade_passed)
    


# s1 = CourseAttempt("Introduction to Programming", 5, 5)
# s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
# s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
# ag = average([s1, s2, s3])
# print(ag)