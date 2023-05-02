#Making a GPA calculator

#importing the os module to save the variable to a text file
import os

#Creating a class calculator with the attributes name, credits and grade
class Calculator:
    def __init__(self, name, credits, grade):
        self.name = name
        self.credits = credits
        self.grade = grade

#creating a function to assign the grades A to F with grade point 4.0 to 0.0
    def grade_point(self):
        if self.grade == "A":
            return 4.0
        elif self.grade == "A-":
            return 3.7
        elif self.grade == "B+":
            return 3.3
        elif self.grade == "B":
            return 3.0
        elif self.grade == "B-":
            return 2.7
        elif self.grade == "C+":
            return 2.3
        elif self.grade == "C":
            return 2.0
        elif self.grade == "C-":
            return 1.7
        elif self.grade == "D+":
            return 1.3
        elif self.grade == "D":
            return 1.0
        elif self.grade == "F":
            return 0.0
        else:
            return None

#creating a class student to make name as an attribute and also making a list attribute courses 
class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

#creating a function to append the course in the list
    def add_course(self, name, credits, grade):
        course = Calculator(name, credits, grade)
        self.courses.append(course)

#creating a function to get the GPA of the student by using the formula of adding the credits and then averaging it out
    def calculate_gpa(self):
        total_grade_points = 0
        total_credits = 0

#using loops and conditions to calculate the GPA       
        for course in self.courses:
            grade_points = course.grade_point()
            if grade_points is not None:
                total_grade_points = total_grade_points + grade_points * course.credits
                total_credits = total_credits + course.credits
        
        if total_credits == 0:
            return None
        else:
            return total_grade_points / total_credits

#taking user input about their name and then using a class using that data
student_name = input("Enter the student name: ")
student = Student(student_name)

#taking user input about their courses, course grade, and the credits of their course and then putting that data into a class
while True:
    course_name = input("Enter course name (or 'f' to finish): ")
    if course_name == "f":
        break
    else:
        credits = int(input("Enter the credits in that class: "))
        grade = input("Enter your class grade (A, A-, B+, B, B-, C+, C, C-, D+, D, F): ")
        student.add_course(course_name, credits, grade)


#Printing out the student name and their GPA
gpa = student.calculate_gpa()
if gpa is not None:
    print(f"{student.name}'s GPA is {gpa:.2f}")
else:
    print("No courses are found.")


#saving the variable values stusent name and gpa to a text file result.txt
file_path = os.path.join(os.getcwd(), 'result.txt')
with open(file_path, 'w') as file:
    file.write('student_name = {}\n'.format(student_name))
    file.write('gpa = {}\n'.format(gpa))


file.close()