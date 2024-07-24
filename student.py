from gradebook import *
class Student:

    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        total_credits = sum(course['credits'] for course in self.courses_registered)
        if total_credits == 0:
            self.GPA = 0.0
        else:
            total_points = sum(course['grade'] * course['credits'] for course in self.courses_registered)
            self.GPA = total_points / total_credits
        print(self.GPA)

    def register_for_course(self, course):
        self.courses_registered.append(course)
        print(self.courses_registered)

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
