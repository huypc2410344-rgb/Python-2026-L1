# ==========================================
# CLASSES DEFINITION (OOP)
# ==========================================

class Student:
    def __init__(self):
        # Proper encapsulation: Using private attributes (__)
        self.__id = ""
        self.__name = ""
        self.__dob = ""

    # Proper polymorphism: .input() method for Student
    def input(self):
        self.__id = input("  Student ID: ")
        self.__name = input("  Student Name: ")
        self.__dob = input("  Date of Birth (DD/MM/YYYY): ")

    # Proper polymorphism: .list() method for Student
    def list(self):
        print(f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}")

    # Getters to access private attributes
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class Course:
    def __init__(self):
        # Proper encapsulation: Using private attributes (__)
        self.__id = ""
        self.__name = ""

    # Proper polymorphism: .input() method for Course
    def input(self):
        self.__id = input("  Course ID: ")
        self.__name = input("  Course Name: ")

    # Proper polymorphism: .list() method for Course
    def list(self):
        print(f"ID: {self.__id} | Course Name: {self.__name}")

    def get_id(self):
        return self.__id


class MarkManagementSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {} # Dictionary to store marks

    def input_students(self):
        try:
            num = int(input("Enter the number of students: "))
            print(f"\n--- ENTERING INFORMATION FOR {num} STUDENTS ---")
            for i in range(num):
                print(f"Student #{i+1}:")
                # Create a new Student object
                student = Student() 
                student.input()
                self.__students.append(student)
            print("-> Students added successfully!\n")
        except ValueError:
            print("Invalid input! Please enter a number.")

    def input_courses(self):
        try:
            num = int(input("Enter the number of courses: "))
            print(f"\n--- ENTERING INFORMATION FOR {num} COURSES ---")
            for i in range(num):
                print(f"Course #{i+1}:")
                # Create a new Course object
                course = Course()
                course.input()
                self.__courses.append(course)
            print("-> Courses added successfully!\n")
        except ValueError:
            print("Invalid input! Please enter a number.")

    def list_students(self):
        print("\n--- STUDENT LIST ---")
        if not self.__students:
            print("Empty.")
        for student in self.__students:
            student.list()

    def list_courses(self):
        print("\n--- COURSE LIST ---")
        if not self.__courses:
            print("Empty.")
        for course in self.__courses:
            course.list()

    def input_marks(self):
        if not self.__courses or not self.__students:
            print("Please input both students and courses first!")
            return
            
        self.list_courses()
        c_id = input("\nEnter Course ID to input marks: ")
        
        # Check if the course exists by checking all course objects
        if not any(c.get_id() == c_id for c in self.__courses):
            print("Course ID does not exist!")
            return
            
        if c_id not in self.__marks:
            self.__marks[c_id] = {}
            
        print(f"\n--- INPUTTING MARKS FOR COURSE: {c_id} ---")
        for student in self.__students:
            while True:
                try:
                    mark = float(input(f"Enter mark for {student.get_name()} (ID: {student.get_id()}): "))
                    if 0 <= mark <= 20:
                        self.__marks[c_id][student.get_id()] = mark
                        break
                    else:
                        print("Mark must be between 0 and 20.")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
        print("-> Marks recorded successfully!\n")

    def show_marks(self):
        if not self.__marks:
            print("No marks have been recorded yet!")
            return

        self.list_courses()
        c_id = input("\nEnter Course ID to view marks: ")
        
        if c_id in self.__marks:
            print(f"\n--- MARK SHEET FOR COURSE: {c_id} ---")
            for student in self.__students:
                s_id = student.get_id()
                mark = self.__marks[c_id].get(s_id, "Not graded")
                print(f"Student: {student.get_name()} (ID: {s_id}) -> Mark: {mark}")
        else:
            print("No marks found for this course or Course ID is incorrect!")

# ==========================================
# MAIN EXECUTION
# ==========================================

def main():
    # Instantiate the management system
    system = MarkManagementSystem()
    
    while True:
        print("\n" + "="*45)
        print("   OOP STUDENT MARK MANAGEMENT - PRACTICAL WORK 2")
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
            system.input_students()
        elif choice == '2':
            system.input_courses()
        elif choice == '3':
            system.input_marks()
        elif choice == '4':
            system.list_students()
        elif choice == '5':
            system.list_courses()
        elif choice == '6':
            system.show_marks()
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()