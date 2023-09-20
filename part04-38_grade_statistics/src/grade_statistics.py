# Write your solution here


def main ():
    exerpoints = []
    exmpoints = []
    grad = []
    while True:
        numbers = input("Exam points and excercises completed: ")
        if numbers == "":
            break
        complet_ex = exercises_completed(numbers)
        exm_points = points_from_exam(numbers)
        points_from_exercise = exercise_points(complet_ex)
        grading = grade(exm_points, points_from_exercise)
        exerpoints.append(points_from_exercise)
        exmpoints.append(exm_points)
        grad.append(grading)
    print("Statistics:")
    average = average_points (exmpoints, exerpoints, grad)
    passing = precent_of_pass (grad)
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {passing:.1f}")
    print("Grade distribution: ")
    grade_distribution (grad)

    
def exercises_completed (points: str):
    space = points.find(" ")
    first = points[:space]
    second = points[space:]
    exam_points = int(first)
    completed_excercises = int(second)
    return completed_excercises

def points_from_exam (points: str):
    space = points.find(" ")
    first = points[:space]
    second = points[space:]
    exam_points = int(first)
    return exam_points

def exercise_points (number: int):
    points = number // 10
    return points

def grade (xmpoints: int, ecspoints: int):
    if xmpoints < 10:
        grade = 0
        return grade

    number = xmpoints + ecspoints
    if number <= 14:
        grade = 0
    elif number > 14 and number <= 17:
        grade = 1
    elif number > 17 and number <= 20:
        grade = 2
    elif number > 20 and number <= 23:
        grade = 3
    elif number > 23 and number <= 27:
        grade = 4
    else:
        grade = 5
    return grade


def average_points (xmpoints: list, ecspoints: list, grades: list):
    return (sum(xmpoints) + sum(ecspoints)) / len(grades)

def precent_of_pass (grades: list):
    counter = 0
    for number in grades:
        if number > 0:
            counter += 1
    return (counter / len(grades)) * 100

def grade_distribution (grades: list):
    star = "*"
    fives = 0 
    fours = 0
    threes = 0
    twos = 0
    ones = 0
    zeros = 0
    for number in grades: 
        if number == 5:
            fives += 1
        if number == 4:
            fours += 1
        if number == 3:
            threes += 1
        if number == 2:
            twos += 1
        if number == 1:
            ones += 1
        if number == 0:
            zeros += 1
    print(f"  5: {fives * star}")
    print(f"  4: {fours * star}")
    print(f"  3: {threes * star}")
    print(f"  2: {twos * star}")
    print(f"  1: {ones * star}")
    print(f"  0: {zeros * star}")


main()


# if __name__ == "__main__":
#     points = [4,5,3,2,2,2,2,1,1,3,3,4,4,5,5]
#     result = grade_distribution(points)
#     print (result)




