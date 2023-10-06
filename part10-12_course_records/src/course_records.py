

class Course: 
    def __init__(self, name: str, credits: int, grade: int):
        self.__name = name
        self.__credits = credits
        self.__grade = grade
        
    def get_name(self):
        return self.__name
    
    def get_credits(self):
        return self.__credits
    
    def get_grade(self):
        return self.__grade
        
class MyCourses: 
    def __init__(self):
        self.__courses = {}
        
    def add_course(self, name: str, credits: int, grade: int):
        if name in self.__courses:
            if grade <= int(self.__courses[name][1]):
                return
        self.__courses[name] = credits, grade
        
    def number_of_courses(self):
        return len(self.__courses)
    
    def total_credits(self):
        tot_credits = 0
        for course in self.__courses.values():
            tot_credits += int(course[0])
        return tot_credits            
    
    def grade_mean(self): 
        gpa = 0
        for course in self.__courses.values():
            gpa += int(course[1])
        return '{0:.1f}'.format(gpa / self.number_of_courses())
    
    def get_course(self, name:str): 
        if name in self.__courses: 
            return self.__courses[name]
        else: 
            return None     

    def grade_distribution(self, grade: int):
        amount = 0
        for course in self.__courses.values():
            if int(course[1]) == grade:
                amount += 1
        return amount
                   
    def __str__(self):
        return f"{self.number_of_courses()} completed courses, a total of {self.total_credits()} credits\nmean {self.grade_mean()}"
          
                  
class CourseApplication: 
    def __init__(self):
        self.__my_courses = MyCourses()
        
    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
    
    def execute(self):
        self.help()
        while True:
            command = int(input("command: "))
            if command == 0: 
                break
            elif command == 1: 
                name = input("course: ")
                grade = int(input("grade: "))
                credits = int(input("credits: "))
                self.__my_courses.add_course(name, credits, grade)
            elif command == 2:
                name = input("course: ")
                course_info = self.__my_courses.get_course(name)
                if course_info == None: 
                    print("no entry for this course")
                else: 
                    print(f"{name} ({course_info[0]} cr) grade {course_info[1]}")
            elif command == 3:
                print(self.__my_courses)
                print("grade distribution")
                five = self.__my_courses.grade_distribution(5)
                four = self.__my_courses.grade_distribution(4)
                three = self.__my_courses.grade_distribution(3)
                two = self.__my_courses.grade_distribution(2)
                one = self.__my_courses.grade_distribution(1)
                ex = "x"
               
                print(f"5: {ex*five}")
                print(f"4: {ex*four}")
                print(f"3: {ex*three}")
                print(f"2: {ex*two}")
                print(f"1: {ex*one}")
                
            

app = CourseApplication()
app.execute()
        
