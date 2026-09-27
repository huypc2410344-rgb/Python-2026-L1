students = []
courses = []
marks = {} 

def input_students():
    n = int(input("Number of students: "))
    for i in range(n):
        s_id = input("NickName: ")
        s_name = input("Name: ")
        s_dob = input("DoB: ")
        students.append({'id': s_id, 'name': s_name, 'dob': s_dob})

def input_courses():
    n = int(input("Number of courses: "))
    for i in range(n):
        c_id = input("Course ID: ")
        c_name = input("Course Name: ")
        courses.append({'id': c_id, 'name': c_name})

def input_marks():
    if not courses or not students:
        print("Missing students or courses!")
        return

    list_courses()
    c_id = input("Enter Course ID for marks: ")
    
    if any(c['id'] == c_id for c in courses):
        marks[c_id] = {}
        for s in students:
            m = float(input(f"Mark for {s['name']}: "))
            marks[c_id][s['id']] = m
    else:
        print("Invalid Course ID!")

def list_courses():
    for c in courses:1
    print(f"ID: {c['id']} | Name: {c['name']}")

def list_students():
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def show_student_marks():
    c_id = input("Enter Course ID to view marks: ")
    if c_id in marks:
        for s in students:
            m = marks[c_id].get(s['id'], "N/A")
            print(f"Student: {s['name']} - Mark: {m}")
    else:
        print("No marks found!")

def main():
    while True:
        print("\n1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List courses")
        print("5. List students")
        print("6. Show marks")
        print("0. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1': input_students()
        elif choice == '2': input_courses()
        elif choice == '3': input_marks()
        elif choice == '4': list_courses()
        elif choice == '5': list_students()
        elif choice == '6': show_student_marks()
        elif choice == '0': break

if __name__ == "__main__":
    main()