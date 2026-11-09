# =========== PROJECT 3 ============
# STUDENT MANAGEMENT SYSTEM
students = {} # Stores all the student's records

def add_student():
    student_id = int(input("Enter the student's ID: ")) # Gets student ID
    
    while len(student_id) != 8 :
        print("Please enter an ID with 8 digits!")
        student_id = int(input("Re-enter the ID: "))
    while not student_id.isdigit():
        print("ID inserted has letters")
        print("ID should only have digits")
        student_id = int(input("Re-enter the ID: "))
    while student_id in students:
        print("This ID belongs to someone else! ")
        student_id = int(input("Enter another ID: "))
        
        while len(student_id) != 8:
            print("please enter an ID with 8 digits! ")
            student_id = int(input("Re-enter the ID: "))
        while not student_id.isdigit():
            print("The ID inserted has letters!")
            print("ID should only have digits")
            student_id = int(input("Re-enter the ID: "))
    
    name = input("Enter Student's name: ")
    age = int(input("Enter the student's age: "))
    
    while age < 15 or age > 45:
        print("Age must be between 15 & 45")
        age = int(input("Re-enter the student age"))
    
    major = input("Enter the student's major: ")
    email =  student_id + "@sycu.edu"
    
    # Stores the student's information
    students[student_id] = {  # This line means that the student's id becomes the dictionary key
        "name": name,
        "age": age,
        "major": major,
        "email": email,
        "scores": [] # Stores an empty score list
    }
    
    print("Student added successfully. ")
    
    