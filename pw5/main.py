import curses
from input import input_students, input_courses, input_marks
from output import calculate_gpa, show_students_and_marks
from compression import save_and_compress, decompress_and_load

def main(stdscr):
    students = []
    courses = []
    marks = {}
    
    # 1. Automatically check and decompress data from students.dat on startup
    decompress_and_load(students, courses, marks)
    
    while True:
        stdscr.clear()
        stdscr.addstr("=========================================\n", curses.A_BOLD)
        stdscr.addstr(" PRACTICAL WORK 5: PERSISTENT INFO\n", curses.A_BOLD)
        stdscr.addstr("=========================================\n")
        stdscr.addstr("1. Input students\n")
        stdscr.addstr("2. Input courses\n")
        stdscr.addstr("3. Input marks\n")
        stdscr.addstr("4. Show students & GPA\n")
        stdscr.addstr("0. Exit & Save (Compress to students.dat)\n")
        stdscr.addstr("=========================================\n")
        stdscr.addstr("Select an option: ")
        
        curses.echo()
        choice = stdscr.getstr().decode('utf-8')
        
        if choice == '1':
            input_students(stdscr, students)
        elif choice == '2':
            input_courses(stdscr, courses)
        elif choice == '3':
            input_marks(stdscr, students, courses, marks)
            calculate_gpa(students, courses, marks)
        elif choice == '4':
            show_students_and_marks(stdscr, students)
        elif choice == '0':
            # 2. Compress and save all information before closing the program
            save_and_compress(students, courses, marks)
            break

if __name__ == "__main__":
    curses.wrapper(main)