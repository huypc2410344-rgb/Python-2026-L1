import curses
import math
import numpy as np

# ==========================================
# CLASSES DEFINITION (OOP + MATH + NUMPY)
# ==========================================

class Student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__dob = ""
        self.__gpa = 0.0  # Added GPA attribute

    def input(self, stdscr):
        curses.echo() # Hiện chữ khi gõ
        stdscr.addstr("  Student ID: ")
        self.__id = stdscr.getstr().decode('utf-8')
        stdscr.addstr("  Student Name: ")
        self.__name = stdscr.getstr().decode('utf-8')
        stdscr.addstr("  Date of Birth (DD/MM/YYYY): ")
        self.__dob = stdscr.getstr().decode('utf-8')

    def list(self, stdscr):
        stdscr.addstr(f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob} | GPA: {self.__gpa:.2f}\n")

    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def set_gpa(self, gpa): self.__gpa = gpa
    def get_gpa(self): return self.__gpa

class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__credits = 0 # Added credits for GPA calculation

    def input(self, stdscr):
        curses.echo()
        stdscr.addstr("  Course ID: ")
        self.__id = stdscr.getstr().decode('utf-8')
        stdscr.addstr("  Course Name: ")
        self.__name = stdscr.getstr().decode('utf-8')
        stdscr.addstr("  Credits: ")
        try:
            self.__credits = int(stdscr.getstr().decode('utf-8'))
        except ValueError:
            self.__credits = 1 # Default 1 if invalid

    def list(self, stdscr):
        stdscr.addstr(f"ID: {self.__id} | Name: {self.__name} | Credits: {self.__credits}\n")

    def get_id(self): return self.__id
    def get_credits(self): return self.__credits


class MarkSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}

    def input_students(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Enter number of students: ")
        try:
            num = int(stdscr.getstr().decode('utf-8'))
            for i in range(num):
                stdscr.addstr(f"\nStudent #{i+1}:\n")
                s = Student()
                s.input(stdscr)
                self.__students.append(s)
            stdscr.addstr("\n-> Students added! Press any key to return...")
        except ValueError:
            stdscr.addstr("\nInvalid input! Press any key...")
        stdscr.getch()

    def input_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Enter number of courses: ")
        try:
            num = int(stdscr.getstr().decode('utf-8'))
            for i in range(num):
                stdscr.addstr(f"\nCourse #{i+1}:\n")
                c = Course()
                c.input(stdscr)
                self.__courses.append(c)
            stdscr.addstr("\n-> Courses added! Press any key to return...")
        except ValueError:
            stdscr.addstr("\nInvalid input! Press any key...")
        stdscr.getch()

    def input_marks(self, stdscr):
        stdscr.clear()
        if not self.__courses or not self.__students:
            stdscr.addstr("Please input both students and courses first! Press any key...")
            stdscr.getch()
            return
            
        stdscr.addstr("--- COURSE LIST ---\n")
        for c in self.__courses:
            c.list(stdscr)
            
        stdscr.addstr("\nEnter Course ID to input marks: ")
        c_id = stdscr.getstr().decode('utf-8')
        
        if not any(c.get_id() == c_id for c in self.__courses):
            stdscr.addstr("\nCourse ID does not exist! Press any key...")
            stdscr.getch()
            return
            
        if c_id not in self.__marks:
            self.__marks[c_id] = {}
            
        stdscr.addstr(f"\n--- INPUTTING MARKS FOR COURSE: {c_id} ---\n")
        for student in self.__students:
            stdscr.addstr(f"Enter mark for {student.get_name()} (ID: {student.get_id()}): ")
            try:
                raw_mark = float(stdscr.getstr().decode('utf-8'))
                # Use math.floor() to round down to 1 decimal digit
                rounded_mark = math.floor(raw_mark * 10) / 10.0
                self.__marks[c_id][student.get_id()] = rounded_mark
            except ValueError:
                stdscr.addstr("Invalid. Setting mark to 0.\n")
                self.__marks[c_id][student.get_id()] = 0.0
                
        self.calculate_gpa() # Cập nhật lại GPA sau khi nhập điểm
        stdscr.addstr("\n-> Marks recorded! Press any key...")
        stdscr.getch()

    def calculate_gpa(self):
        """Sử dụng Numpy array để tính tổng trọng số và điểm GPA"""
        for student in self.__students:
            marks_list = []
            credits_list = []
            for course in self.__courses:
                c_id = course.get_id()
                if c_id in self.__marks and student.get_id() in self.__marks[c_id]:
                    marks_list.append(self.__marks[c_id][student.get_id()])
                    credits_list.append(course.get_credits())
            
            if credits_list:
                np_marks = np.array(marks_list)
                np_credits = np.array(credits_list)
                # Weighted sum of credits and marks
                gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
                student.set_gpa(gpa)
            else:
                student.set_gpa(0.0)
                
        # Sort student list by GPA descending
        self.__students.sort(key=lambda s: s.get_gpa(), reverse=True)

    def show_students_and_marks(self, stdscr):
        stdscr.clear()
        stdscr.addstr("--- STUDENT LIST (SORTED BY GPA DESCENDING) ---\n")
        if not self.__students:
            stdscr.addstr("Empty.\n")
        for s in self.__students:
            s.list(stdscr)
            
        stdscr.addstr("\nPress any key to return...")
        stdscr.getch()

# ==========================================
# CURSES UI MAIN LOOP
# ==========================================

def main(stdscr):
    system = MarkSystem()
    
    while True:
        stdscr.clear()
        stdscr.addstr("=========================================\n", curses.A_BOLD)
        stdscr.addstr(" PRACTICAL WORK 3: MATHS & DECORATIONS\n", curses.A_BOLD)
        stdscr.addstr("=========================================\n")
        stdscr.addstr("1. Input students\n")
        stdscr.addstr("2. Input courses (with credits)\n")
        stdscr.addstr("3. Input marks (auto-rounded down & updates GPA)\n")
        stdscr.addstr("4. Show students & GPA (Sorted descending)\n")
        stdscr.addstr("0. Exit\n")
        stdscr.addstr("=========================================\n")
        stdscr.addstr("Select an option: ")
        
        curses.echo()
        choice = stdscr.getstr().decode('utf-8')
        
        if choice == '1':
            system.input_students(stdscr)
        elif choice == '2':
            system.input_courses(stdscr)
        elif choice == '3':
            system.input_marks(stdscr)
        elif choice == '4':
            system.show_students_and_marks(stdscr)
        elif choice == '0':
            break

if __name__ == "__main__":
    curses.wrapper(main)