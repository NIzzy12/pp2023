class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Mark:
    def __init__(self, student_id, course_id, value):
        self.student_id = student_id
        self.course_id = course_id
        self.value = value

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_students(self):
        num_students = int(input("Enter number of students: "))
        for i in range(num_students):
            id = input(f"Enter id for student {i+1}: ")
            name = input(f"Enter name for student {i+1}: ")
            dob = input(f"Enter date of birth for student {i+1}: ")
            self.students.append(Student(id, name, dob))

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for i in range(num_courses):
            id = input(f"Enter id for course {i+1}: ")
            name = input(f"Enter name for course {i+1}: ")
            self.courses.append(Course(id, name))

    def input_marks(self):
        for course in self.courses:
            course_id = course.id
            for student in self.students:
                student_id = student.id
                value = int(input(f"Enter mark for {student.name} in course {course_id}: "))
                self.marks.append(Mark(student_id, course_id, value))

    def list_courses(self):
        for course in self.courses:
            print(f"{course.id}: {course.name}")

    def list_students(self):
        for student in self.students:
            print(f"{student.id}: {student.name}")

    def show_student_marks(self, course_id):
        for mark in self.marks:
            if mark.course_id == course_id:
                student_name = next((s.name for s in self.students if s.id == mark.student_id), None)
                if student_name:
                    print(f"{student_name}: {mark.value}")

school = School()
school.input_students()
school.input_courses()
school.input_marks()

while True:
    print("\nMENU")
    print("1. List courses")
    print("2. List students")
    print("3. Show student marks for a course")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        school.list_courses()
    elif choice == 2:
        school.list_students()
    elif choice == 3:
        course_id = input("Enter course id: ")
        school.show_student_marks(course_id)
    elif choice == 4:
        break
    else:
        print("Invalid choice, please try again.")
