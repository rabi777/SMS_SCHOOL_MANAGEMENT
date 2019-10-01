import csv

from Models import Student
from Models import Course
from Models import Attending


class StudentDAO:
    students = []

    def __init__(self):
        with open('students.csv') as file_obj:
            students = csv.reader(file_obj)
            for student in students:
                temp = {}
                temp['email'] = student[0]
                temp['name'] = student[1]
                temp['pass'] = student[2]
                self.students.append(temp)

    def get_students(self):
        return self.students

    def validate_user(self, email, pw):
        if any(student['email'] == email and student['pass'] == pw for student in self.students):
            return True
        else:
            return False

    def get_student_by_email(self, email):
        for student in self.students:
            if student['email'] == email:
                student = Student(student['email'], student['name'], student['pass'])
                return student


class CourseDAO:
    all_course = []

    def __init__(self):
        with open('courses.csv') as file_obj:
            courses = csv.reader(file_obj)
            for course in courses:
                course = Course(course[0], course[1], course[2])
                self.all_course.append(course)

    def get_courses(self):
        return self.all_course


class AttendingDAO:
    attending = []

    def __init__(self):
        with open('attending.csv') as file_obj:
            obj = csv.reader(file_obj)
            for data in obj:
                attend = Attending(data[0], data[1])
                self.attending.append(attend)

    def get_attending(self):
        return self.attending

    def get_student_courses(self, course_list, email):
        courses = list()
        for course in course_list:
            if any(obj.get_student_email() == email and obj.get_course_id() == course.get_id() for obj in
                   self.attending):
                courses.append(course)
        return courses

    def register_student_to_course(self, email, course_id, course_list):
        id = False
        for course in course_list:
            if course.get_id() == course_id:
                id = not id
        is_register = any(obj.get_student_email() == email and obj.get_course_id() == course_id for obj in
                          self.attending)
        if not id:
            pass
        elif is_register:
            print('\nYou Are Already Registered In The Course.')
            return False
        elif id:
            self.save_attending(email, course_id)
            return True

    def save_attending(self, email, course_id):
        path = 'attending.csv'
        attending_data = list()
        attending_data.append([course_id, email])
        with open(path, "a", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in attending_data:
                writer.writerow(line)

        print('\nRegistration Successfull!')
