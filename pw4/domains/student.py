import curses

class Student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__dob = ""
        self.__gpa = 0.0

    def input(self, stdscr):
        curses.echo()
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