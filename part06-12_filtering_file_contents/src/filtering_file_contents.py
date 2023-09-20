# Write your solution here


def filter_solutions():
    with open("solutions.csv") as file:
        students = []
        for line in file:
            line = line.strip()
            line = line.split(";")
            students.append(line)

    with open("correct.csv", "w") as correct_results:
        with open("incorrect.csv", "w") as incorrect_results:
            for student in students: 
                result = eval(student[1])
                ans = int(student[2])
                if result == ans:
                    student = f"{student[0]};{student[1]};{student[2]}"
                    correct_results.write(student+"\n")
                else: 
                    student = f"{student[0]};{student[1]};{student[2]}"
                    incorrect_results.write(student+"\n")
            

if __name__ == "__main__":
    filter_solutions()


