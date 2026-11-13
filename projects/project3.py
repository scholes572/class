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
        students[student_id]["scores"] = scores
            
        print("Scores added successfully :) ")
    else:
        print("We don't have that ID in our systems. Sorry :( ")
            
        
def score_report():
    if len(students) == 0:
        print("No students available.")

    else:
        class_total = 0
        number = 0

        for student_id in students:

            scores = students[student_id]["scores"]

            if len(scores) == 3:

                total = 0

                for score in scores:
                    total = total + score

                average = total / 3

                if average >= 80:
                    grade = "A"
                elif average >= 70:
                    grade = "B"
                elif average >= 60:
                    grade = "C"
                elif average >= 50:
                    grade = "D"
                else:
                    grade = "F"

                students[student_id]["total"] = total
                students[student_id]["average"] = average
                students[student_id]["grade"] = grade

                class_total = class_total + average
                number = number + 1

        if number == 0:
            print("No students have entered all three scores.")

        else:

            # Rank students by average
            student_ids = []

            for student_id in students:
                if len(students[student_id]["scores"]) == 3:
                    student_ids.append(student_id)

            for i in range(len(student_ids)):
                for j in range(i + 1, len(student_ids)):
                    if students[student_ids[i]]["average"] < students[student_ids[j]]["average"]:
                        student_ids[i], student_ids[j] = student_ids[j], student_ids[i]

            # Display ranked results
            print("\n========== RANKED STUDENT RESULTS ==========")
            print("Rank | Name | Total | Average | Grade")

            for i in range(len(student_ids)):
                student_id = student_ids[i]

                print(
                    i + 1, "|",
                    students[student_id]["name"], "|",
                    students[student_id]["total"], "|",
                    round(students[student_id]["average"], 2), "|",
                    students[student_id]["grade"]
                )

            # Calculate class statistics
            class_average = class_total / number

            highest_total = students[student_ids[0]]["total"]

            for student_id in student_ids:
                if students[student_id]["total"] > highest_total:
                    highest_total = students[student_id]["total"]

            # Display statistics
            print("\n========== CLASS STATISTICS ==========")
            print("Number of students:", number)
            print("Class average:", round(class_average, 2))
            print("Highest student total:", highest_total)
            print("Top student:", students[student_ids[0]]["name"])         
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
    elif choice == "6":
        score_report()
    elif choice == "0":
        print("Bye bye :) !!!")
    else:
        print("Sorry, Try again. Don't give up :)")