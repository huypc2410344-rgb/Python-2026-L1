# Global variables to store data
students = []
courses = []
marks = {}

# ==========================================
# INPUT FUNCTIONS
# ==========================================

def input_number_of_students():
    """Input the number of students in a class"""
    while True:
        try:
            num = int(input("Enter the number of students in the class: "))
            if num > 0:
                return num
            print("The number must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def input_student_info(num_students):
    """Input student information: id, name, DoB"""
    print(f"\n--- ENTERING INFORMATION FOR {num_students} STUDENTS ---")
    for i in range(num_students):
        print(f"Student #{i+1}:")
        s_id = input("  Student ID: ")
        s_name = input("  Student Name: ")
        s_dob = input("  Date of Birth (DD/MM/YYYY): ")
        
        student = {
            "id": s_id,
            "name": s_name,
            "dob": s_dob
        }
        students.append(student)
    print("-> Student list has been successfully updated!\n")

def input_number_of_courses():
    """Input the number of courses"""
    while True:
        try:
            num = int(input("Enter the number of courses: "))
            if num > 0:
                return num
            print("The number must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def input_course_info(num_courses):
    """Input course information: id, name"""
    print(f"\n--- ENTERING INFORMATION FOR {num_courses} COURSES ---")
    for i in range(num_courses):
        print(f"Course #{i+1}:")
        c_id = input("  Course ID: ")
        c_name = input("  Course Name: ")
        
        course = {
            "id": c_id,
            "name": c_name
        }
        courses.append(course)
    print("-> Course list has been successfully updated!\n")

def input_marks_for_course():
    """Select a course and input marks for students in this course"""
    if not courses:
        print("No courses available. Please input courses first!")
        return
    if not students:
        print("No students available. Please input students first!")
        return

    list_courses()
    course_id = input("\nEnter the Course ID to input marks: ")
    
    # Check if the course exists
    course_exists = any(c['id'] == course_id for c in courses)
    if not course_exists:
        print("Course ID does not exist!")
        return

    print(f"\n--- INPUTTING MARKS FOR COURSE: {course_id} ---")
    if course_id not in marks:
        marks[course_id] = {} # Initialize a dictionary for this course's marks

    for student in students:
        while True:
            try:
                mark = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
                if 0 <= mark <= 20: # Assuming a 20-point grading scale
                    marks[course_id][student['id']] = mark
                    break
                else:
                    print("Mark must be between 0 and 20.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    print("-> Marks have been successfully recorded!\n")


# ==========================================
# LISTING FUNCTIONS
# ==========================================

def list_courses():
    """List all courses"""
    print("\n--- COURSE LIST ---")
    if not courses:
        print("Empty.")
    else:
        for c in courses:
            print(f"ID: {c['id']} | Course Name: {c['name']}")

def list_students():
    """List all students"""
    print("\n--- STUDENT LIST ---")
    if not students:
        print("Empty.")
    else:
        for s in students:
            print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def show_student_marks():
    """Show student marks for a given course"""
    if not marks:
        print("No marks have been recorded yet!")
        return

    list_courses()
    course_id = input("\nEnter the Course ID to view marks: ")
    
    if course_id in marks:
        print(f"\n--- MARK SHEET FOR COURSE: {course_id} ---")
        for student in students:
            s_id = student['id']
            # Get the mark if it exists, otherwise display 'Not graded'
            student_mark = marks[course_id].get(s_id, "Not graded")
            print(f"Student: {student['name']} (ID: {s_id}) -> Mark: {student_mark}")
    else:
        print("This course has no recorded marks or the Course ID is incorrect!")


# ==========================================
# MAIN MENU
# ==========================================

def main():
    while True:
        print("\n" + "="*45)
        print("   STUDENT MARK MANAGEMENT - PRACTICAL WORK 1")
        print("="*45)
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a given course")
        print("0. Exit")
        print("="*45)
        
        choice = input("Please select an option (0-6): ")
        
        if choice == '1':
            num = input_number_of_students()
            input_student_info(num)
        elif choice == '2':
            num = input_number_of_courses()
            input_course_info(num)
        elif choice == '3':
            input_marks_for_course()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_student_marks()
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()