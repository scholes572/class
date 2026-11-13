# =========== PROJECT 3 ============
# STUDENT MANAGEMENT SYSTEM
# This program lets you add students, see all students,
# search for a student, delete a student, enter scores,
# and view a score report for everyone.

# 'students' is like an address book that holds every student's information.
# It starts out empty.
students = {}  # Stores all the student's records

# This function adds a new student to the address book.
def add_student():
    # Ask the user to type in the student's ID number.
    student_id = (input("Enter the student's ID: "))  # Gets student ID
    
    # Keep asking until the ID is exactly 8 characters long.
    while len(student_id) != 8:
        print("Please enter an ID with 8 digits!")
        student_id = int(input("Re-enter the ID: "))
    # Make sure the ID only contains numbers (no letters).
    while not student_id.isdigit():
        print("ID inserted has letters")
        print("ID should only have digits")
        student_id = int(input("Re-enter the ID: "))
    # Make sure this ID isn't already taken by another student.
    while student_id in students:
        print("This ID belongs to someone else! ")
        student_id = int(input("Enter another ID: "))
        
        # Again, check the ID is 8 characters long.
        while len(student_id) != 8:
            print("please enter an ID with 8 digits! ")
            student_id = int(input("Re-enter the ID: "))
        # Again, check the ID only has digits.
        while not student_id.isdigit():
            print("The ID inserted has letters!")
            print("ID should only have digits")
            student_id = int(input("Re-enter the ID: "))
    
    # Ask for the student's name.
    name = input("Enter Student's name: ")
    # Ask for the student's age and turn it into a whole number.
    age = int(input("Enter the student's age: "))
    
    # Keep asking until the age is between 15 and 45.
    while age < 15 or age > 45:
        print("Age must be between 15 & 45")
        age = int(input("Re-enter the student age"))
    
    # Ask what subject/major the student studies.
    major = input("Enter the student's major: ")
    # Create an email address using the student's ID.
    email =  student_id + "@sycu.edu"
    
    # Save everything about this student under their ID.
    # students[student_id] means: use the student's ID as the key/label.
    students[student_id] = {  # This line means that the student's id becomes dictionary key
        "name": name,
        "age": age,
        "major": major,
        "email": email,
        "scores": []  # Stores an empty score list (no scores yet)
    }
    
    # Tell the user the student was added.
    print("\nStudent added successfully. ")
    

   
# This function shows students that are currently saved.
def view_students():
    # If no students have been added yet, say so.
    if len(students) == 0:
        print("There's no students yet!!!")
    else:
        # Go through each student one by one.
        for student_id in students:
            print("\nStudents ID:", student_id)
            print("Name:",students[student_id]["name"])
            print("Age:", students[student_id]["age"])
            print("Major:", students[student_id]["major"])
            print("Email:", students[student_id]["email"])
            print("Scores:", students[student_id]["scores"] )

# This function looks for a specific student by ID or name.
def search_student():
    # Ask the user what ID or name to look for.
    search = input("Enter the student ID or Name: ").lower()
    # Start a counter at zero to track if we found anyone.
    count = 0
    
    # Go through every student in the list.
    for student_id in students: 
        name = students[student_id]["name"]
        
        # If the ID matches or the name matches, show their details.
        if student_id == search or name.lower() == search.lower():
            print("\nStudent ID:", student_id)
            print("Name:",students[student_id]["name"])
            print("Age:", students[student_id]["age"])
            print("Major:", students[student_id]["major"])
            print("Email:", students[student_id]["email"])
            print("scores:", students[student_id]["scores"])
            count = count + 1 
    # If we never found a match, tell the user.
    if count == 0:
        print("Student not found :( !")

# This function removes a student from the address book.
def delete_student():
    # Ask which student ID to delete.
    student_id = input("You sure about this?...Let's proceed then. Enter student ID: ")
    # If that student exists, remove them.
    if student_id in students:
        del students[student_id]
        print("The student is no longer one of us! :( ")
    else:
        print("Nope!. There's no such student ID in our system!")
        
# This function lets you type in test scores for a student.
def enter_score():
    # Ask which student's scores to enter.
    student_id = input("Enter the student's ID: ")
    # If that student exists, ask for 3 scores.
    if student_id in students:
        scores = []
        for i in range(3):
            score = float(input("Enter the Student's score: "))
            # Keep asking until the score is between 0 and 100.
            while score < 0 or score > 100:
                print("Invalid score! :( !!!")
                score = float(input("Re-enter the student's score: "))
            scores.append(score)
        # Save the 3 scores under the lowercase key "scores".
        students[student_id]["scores"] = scores
            
        print("Scores added successfully :) ")
    else:
        print("We don't have that ID in our systems. Sorry :( ")
                     
# This function shows a report of everyone's scores and grades.
def score_report():
    # If there are no students at all, say so.
    if len(students) == 0:
        print("No students available.")

    else:
        # Get ready to add up all averages and count students.
        class_total = 0
        number = 0

        # Go through each student.
        for student_id in students:

            # Get that student's list of scores.
            scores = students[student_id]["scores"]

            # Only do math if the student has all 3 scores.
            if len(scores) == 3:

                total = 0

                # Add up all 3 scores.
                for score in scores:
                    total = total + score

                # Divide by 3 to get the average.
                average = total / 3

                # Turn the average into a letter grade (A, B, C, D, or F).
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

                # Save the total, average, and grade for this student.
                students[student_id]["total"] = total
                students[student_id]["average"] = average
                students[student_id]["grade"] = grade

                # Add this student's average to the class running total.
                class_total = class_total + average
                # Count how many students have complete scores.
                number = number + 1
                
        # If nobody had all 3 scores, say so.
        if number == 0:
            print("No students have entered all three scores.")

        else:

            # Make a list of student IDs who have complete scores.
            student_ids = []

            for student_id in students:
                if len(students[student_id]["scores"]) == 3:
                    student_ids.append(student_id)

            # Sort the students from highest average to lowest average.
            for i in range(len(student_ids)):
                for j in range(i + 1, len(student_ids)):
                    if students[student_ids[i]]["average"] < students[student_ids[j]]["average"]:
                        student_ids[i], student_ids[j] = student_ids[j], student_ids[i]

            # Show the ranked results table.
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

            # Find the class average.
            class_average = class_total / number

            # Find the highest total score.
            highest_total = students[student_ids[0]]["total"]

            for student_id in student_ids:
                if students[student_id]["total"] > highest_total:
                    highest_total = students[student_id]["total"]

            # Show the class statistics summary.
            print("\n========== CLASS STATISTICS ==========")
            print("Number of students:", number)
            print("Class average:", round(class_average, 2))
            print("Highest student total:", highest_total)
            print("Top student:", students[student_ids[0]]["name"])         

choice = ""
# Keep showing the menu until the user picks "0" to exit.
while choice != "0":
    # Show the menu options.
    print("\n ===== STUDENT MANAGAEMENT SYSTEM =====")
    print("\n1. Add a student!")
    print("2. View all the students!")
    print("3. Search a student")
    print("4. Delete a student!")
    print("5. Enter the student scores!")
    print("6. Thee score report")
    print("0. Exit!!!")
    
    # Ask the user to pick an option.
    choice = input("\nEnter your choice: ")
    # If they picked 1, add a student.
    if choice == "1":
        add_student()
    # If they picked 2, view all students.
    elif choice == "2":
        view_students()
    # If they picked 3, search for a student.
    elif choice == "3":
        search_student()
    # If they picked 4, delete a student.
    elif choice == "4":
        delete_student()
    # If they picked 5, enter scores.
    elif choice == "5":
        enter_score()
    # If they picked 6, show the score report.
    elif choice == "6":
        score_report()
    # If they picked 0, say goodbye and stop.
    elif choice == "0":
        print("Bye bye :) !!!")
    # Otherwise, tell them to try again.
    else:
        print("Sorry, Try again. Don't give up :)")
