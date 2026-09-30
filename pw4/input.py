import curses
import math
from domains.student import Student
from domains.course import Course

def input_students(stdscr, students_list):
    stdscr.clear()
    stdscr.addstr("Enter number of students: ")
    try:
        num = int(stdscr.getstr().decode('utf-8'))
        for i in range(num):
            stdscr.addstr(f"\nStudent #{i+1}:\n")
            s = Student()
            s.input(stdscr)
            students_list.append(s)
        stdscr.addstr("\n-> Students added! Press any key to return...")
    except ValueError:
        stdscr.addstr("\nInvalid input! Press any key...")
    stdscr.getch()

def input_courses(stdscr, courses_list):
    stdscr.clear()
    stdscr.addstr("Enter number of courses: ")
    try:
        num = int(stdscr.getstr().decode('utf-8'))
        for i in range(num):
            stdscr.addstr(f"\nCourse #{i+1}:\n")
            c = Course()
            c.input(stdscr)
            courses_list.append(c)
        stdscr.addstr("\n-> Courses added! Press any key to return...")
    except ValueError:
        stdscr.addstr("\nInvalid input! Press any key...")
    stdscr.getch()

def input_marks(stdscr, students_list, courses_list, marks_dict):
    stdscr.clear()
    if not courses_list or not students_list:
        stdscr.addstr("Please input both students and courses first! Press any key...")
        stdscr.getch()
        return
        
    stdscr.addstr("--- COURSE LIST ---\n")
    for c in courses_list:
        c.list(stdscr)
        
    stdscr.addstr("\nEnter Course ID to input marks: ")
    c_id = stdscr.getstr().decode('utf-8')
    
    if not any(c.get_id() == c_id for c in courses_list):
        stdscr.addstr("\nCourse ID does not exist! Press any key...")
        stdscr.getch()
        return
        
    if c_id not in marks_dict:
        marks_dict[c_id] = {}
        
    stdscr.addstr(f"\n--- INPUTTING MARKS FOR COURSE: {c_id} ---\n")
    for student in students_list:
        stdscr.addstr(f"Enter mark for {student.get_name()} (ID: {student.get_id()}): ")
        try:
            raw_mark = float(stdscr.getstr().decode('utf-8'))
            rounded_mark = math.floor(raw_mark * 10) / 10.0
            marks_dict[c_id][student.get_id()] = rounded_mark
        except ValueError:
            stdscr.addstr("Invalid. Setting mark to 0.\n")
            marks_dict[c_id][student.get_id()] = 0.0
            
    stdscr.addstr("\n-> Marks recorded! Press any key...")
    stdscr.getch()