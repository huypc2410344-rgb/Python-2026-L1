import curses

class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__credits = 0

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
            self.__credits = 1

    def list(self, stdscr):
        stdscr.addstr(f"ID: {self.__id} | Name: {self.__name} | Credits: {self.__credits}\n")

    def get_id(self): return self.__id
    def get_credits(self): return self.__credits