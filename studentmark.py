# Input functions
def input_num_students():
    num_students = int(input("Enter number of students: "))
    return num_students

def input_student_info():
    student_info = []
    for i in range(num_students):
        id = input(f"Enter id for student {i+1}: ")
        name = input(f"Enter name for student {i+1}: ")
        dob = input(f"Enter date of birth for student {i+1}: ")
        student_info.append({'id': id, 'name': name, 'dob': dob})
    return student_info

def input_num_courses():
    num_courses = int(input("Enter number of courses: "))
    return num_courses

def input_course_info():
    course_info = []
    for i in range(num_courses):
        id = input(f"Enter id for course {i+1}: ")
        name = input(f"Enter name for course {i+1}: ")
        course_info.append({'id': id, 'name': name})
    return course_info

def input_course_marks(course_id):
    course_marks = []
    for student in student_info:
        mark = int(input(f"Enter mark for {student['name']} in course {course_id}: "))
        course_marks.append({'id': student['id'], 'mark': mark})
    return course_marks

# Listing functions
def list_courses():
    for course in course_info:
        print(f"{course['id']}: {course['name']}")

def list_students():
    for student in student_info:
        print(f"{student['id']}: {student['name']}")

def show_student_marks(course_id):
    for mark in course_marks:
        if mark['id'] == student['id']:
            print(f"{student['name']}: {mark['mark']}")

# Main program
num_students = input_num_students()
student_info = input_student_info()
num_courses = input_num_courses()
course_info = input_course_info()

# Loop through each course to input marks for each student
for course in course_info:
    course_id = course['id']
    course_marks = input_course_marks(course_id)

# Display menu and handle user input
while True:
    print("\nMENU")
    print("1. List courses")
    print("2. List students")
    print("3. Show student marks for a course")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        list_courses()
    elif choice == 2:
        list_students()
    elif choice == 3:
        course_id = input("Enter course id: ")
        show_student_marks(course_id)
    elif choice == 4:
        break
    else:
        print("Invalid choice, please try again.")
        
