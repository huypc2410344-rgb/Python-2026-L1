import curses
import numpy as np

def calculate_gpa(students_list, courses_list, marks_dict):
    for student in students_list:
        marks = []
        credits = []
        for course in courses_list:
            c_id = course.get_id()
            if c_id in marks_dict and student.get_id() in marks_dict[c_id]:
                marks.append(marks_dict[c_id][student.get_id()])
                credits.append(course.get_credits())
        
        if credits:
            np_marks = np.array(marks)
            np_credits = np.array(credits)
            gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
            student.set_gpa(gpa)
        else:
            student.set_gpa(0.0)
            
    students_list.sort(key=lambda s: s.get_gpa(), reverse=True)

def show_students_and_marks(stdscr, students_list):
    stdscr.clear()
    stdscr.addstr("--- STUDENT LIST (SORTED BY GPA DESCENDING) ---\n")
    if not students_list:
        stdscr.addstr("Empty.\n")
    for s in students_list:
        s.list(stdscr)
        
    stdscr.addstr("\nPress any key to return...")
    stdscr.getch()