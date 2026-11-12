# =========== PROJECT 3 ============
# STUDENT MANAGEMENT SYSTEM
students = {} # Stores all the student's records

def add_student():
    student_id = (input("Enter the student's ID: ")) # Gets student ID
    
    while len(student_id) != 8:
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
    
    # Storage of student information. 
    students[student_id] = {  # This line means that the student's id becomes the dictionary key
        "name": name,
        "age": age,
        "major": major,
        "email": email,
        "scores": [] # Stores an empty score list
    }
    
    print("\nStudent added successfully. ")
    
    
    
def view_students():
    if len(students) == 0:
        print("There's no students yet!!!")
    else:
        for student_id in students:
            print("\nStuidents ID:", student_id)
            print("Name:",students[student_id]["name"])
            print("Age:", students[student_id]["age"])
            print("Major:", students[student_id]["major"])
            print("Email:", students[student_id]["email"])
            print("Scores:", students[student_id]["scores"] )




def search_student():
    search = input("Enter the student ID or Name: ").lower()
    count = 0
    
    for student_id in students: 
        name = students[student_id]["name"]
        
        if student_id == search or name.lower() == search.lower():
            print("\nStudent ID:", student_id)
            print("Name:",students[student_id]["name"])
            print("Age:", students[student_id]["age"])
            print("Major:", students[student_id]["major"])
            print("Email:", students[student_id]["email"])
            print("scores:", students[student_id]["scores"])
            count = count + 1 
    if count == 0:
        print("Student not found :( !")



def delete_student():
    student_id = input("You sure about this?...Let's proceed then. Enter student ID: ")
    if student_id in students:
        del students[student_id]
        print("The student is no longer one of us! :( ")
    else:
        print("Nope!. There's no such student ID in our system!")
        


def enter_score():
    student_id = input("Enter the student's ID: ")
    if student_id in students:
        scores = []
        for i in range(3):
            score = float(input("Enter the Student's score: "))
            while score < 0 or score > 100:
                print("Invalid score! :( !!!")
                score = float(input("Re-enter the student's score: "))
            scores.append(score)
        students[student_id]["Scores"] = scores
            
        print("Scores added successfully :) ")
    else:
        print("We don't have that ID in our systems. Sorry :( ")
            
            
            
choice = ""
while choice != "0":
    print("\n ===== STUDENT MANAGAEMENT SYSTEM =====")
    print("\n1. Add a student!")
    print("2. View all the students!")
    print("3. Search a student")
    print("4. Delete a student!")
    print("5. Enter the student scores!")
    print("6. Thee score report")
    print("0. Exit!!!")
    
    choice = input("\nEnter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        enter_score()
    elif choice == "0":
        print("Bye bye :) !!!")
    else:
        print("Sorry, Try again. Don't give up :)")