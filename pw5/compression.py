import os
import zipfile
from domains.student import Student
from domains.course import Course

def save_and_compress(students, courses, marks):
    """Save data to txt files and compress into students.dat before exiting"""
    # 1. Write data to temporary text files
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.get_id()},{s.get_name()},{s._Student__dob},{s.get_gpa()}\n")

    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")

    with open("marks.txt", "w", encoding="utf-8") as f:
        for c_id, s_marks in marks.items():
            for s_id, mark in s_marks.items():
                f.write(f"{c_id},{s_id},{mark}\n")

    # 2. Use zipfile to compress all txt files into students.dat
    with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zf:
        if os.path.exists("students.txt"): zf.write("students.txt")
        if os.path.exists("courses.txt"): zf.write("courses.txt")
        if os.path.exists("marks.txt"): zf.write("marks.txt")

    # 3. Remove temporary text files to keep the directory clean
    if os.path.exists("students.txt"): os.remove("students.txt")
    if os.path.exists("courses.txt"): os.remove("courses.txt")
    if os.path.exists("marks.txt"): os.remove("marks.txt")

def decompress_and_load(students, courses, marks):
    """Check for students.dat on startup, decompress and load data"""
    if not os.path.exists("students.dat"):
        return # If the compressed file doesn't exist, skip and start fresh

    # 1. Decompress data from students.dat
    with zipfile.ZipFile("students.dat", "r") as zf:
        zf.extractall()

    # 2. Read and load Students data
    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    s = Student()
                    s._Student__id = parts[0]
                    s._Student__name = parts[1]
                    s._Student__dob = parts[2]
                    s.set_gpa(float(parts[3]))
                    students.append(s)

    # 3. Read and load Courses data
    if os.path.exists("courses.txt"):
        with open("courses.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    c = Course()
                    c._Course__id = parts[0]
                    c._Course__name = parts[1]
                    c._Course__credits = int(parts[2])
                    courses.append(c)

    # 4. Read and load Marks data
    if os.path.exists("marks.txt"):
        with open("marks.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    c_id, s_id, mark = parts[0], parts[1], float(parts[2])
                    if c_id not in marks:
                        marks[c_id] = {}
                    marks[c_id][s_id] = mark

    # Clean up text files after loading data into RAM
    if os.path.exists("students.txt"): os.remove("students.txt")
    if os.path.exists("courses.txt"): os.remove("courses.txt")
    if os.path.exists("marks.txt"): os.remove("marks.txt")