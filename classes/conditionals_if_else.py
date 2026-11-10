# ============================================================
# TOPIC: Conditionals - if / elif / else
# Consolidated from: class, class6, class12, class14, class16, class17, class18
# ============================================================

# ---------- yes / no if-else (from class) ----------
answer = input("Type yes or no: ")
if answer == "yes":
    print("You said yes.")
else:
    print("You said no. ")

print()

# ---------- Operator calculator if/elif/else (from class6) ----------
num1 = int(input("Enter first number: "))
operator = input("Choose any operator: ")
num2 = int(input("Enter the second number: "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("ERROR....")

print()

# ---------- Age qualification + admin check (from class12) ----------
age = int(input("What's your age? "))
if age >= 18:
    print("You're qualified")
else:
    print("Not qualified")

name = (input("Name: ").upper)
if name == "ADMIN":
    print("Welcome")
else:
    print("Access denied")

print()

# ---------- Age / money / login / grade (commented, from class14) ----------
# age = int(input("Age: "))
# money = int(input("Money: "))
# if age >= 18 and money > 0:
#     print("Can buy ticket")
# if age < 18 or money <= 0:
#     print("Cannot buy")
# if not (age >= 18):
#     print("minor")
# if age >= 13 and age <= 19:
#     print("Teen")

# # TASK B
# user = input("Username: ")
# pw = input("Pssword: ")
# if user == "admin" and pw == "1234":
#     print("Login successful!")
#     print("Welcome, admin!")
# if user != "admin" or pw != "1234":
#     print("Login failed")

# print("=== Grade Checker ===")
# name = input("Name: ")
# score = int(input("Score: "))
# att = int(input("Attendance %: "))
# if score >= 90:
#     print("Excellent!")
# elif score >= 60:
#     print(f"{name}, you PASSED!")
#     print(f"Your score: {score}/100")
#     print("Good job on the score!")
# else:
#     print(f"{name}, You FAILED!")
#     print(f"Your score: {score}/100")
#     print("Keep practicing!")
# if score >= 60 and att >= 75:
#     print("You passed! ")
# else:
#     print("You failed because of the attendance")

print()

# ---------- Grade calculator if/elif/else (active, from class16) ----------
print("=== Grade Calculator ===")
name = input("What is your name: ")
score = int(input("Insert score between (0-100)"))
score2 = int(input("Insert score 2 between (0-100)"))
score3 = int(input("Insert score 3 between (0-100)"))
average = (score + score2 + score3) / 3

if average < 0 or average > 100:
    print("Invalid Score!")

if average >= 95:
    grade = "A+"
    msg = "Excellent!"
    if average >= 90:
        grade = "A"
        msg = "Impressive!"
elif average >= 85:
    grade = "B+"
    msg = "Very Good job!"
    if average >= 80:
        grade = "B"
        msg = "Good job"
elif average >= 75:
    grade = "C+"
    msg = "Quite good!"
    if average >= 70:
        grade = "C"
        msg = "Not bad!"
elif average >= 60:
    grade = "D+"
    msg = "Needs Improvemnt"
    if average >= 65:
        grade = "D"
        msg = "You getting there"
else:
    grade = "E"
    msg = "Keep studying!"

print(f"{name}: {grade} - {msg}")
print("=== Done ===")

print()

# ---------- Labs 1-6 (commented) + Lab 7 constraints (active, from class17) ----------
# print("===== Lab 1: Task =====")
# task = input("What do you want AI to do? ")
# print("Your task:", task)
# print(f"Length: {len(task)} characters")

# print("===== Lab 2: Task check =====")
# task = input("Task: ")
# if len(task) == 0:
#     print("Missing task! AI does not know what to do. ")
# else:
#     print("Task is written. ")

# print("===== Lab 3: Task quality =====")
# task = input("Task: ")
# if len(task) == 0:
#     print("Level 0: No task.")
# elif len(task) < 10:
#     print("Level 1: too short. Add a verb + an object. ")
# else:
#     print("level 2: clear task. ")

# print("===== Lab 4: Background =====")
# background = input("Background (who you are): ")
# if "student" in background or "teacher" in background or "I am" in background:
#     print("Background OK. ")
# else:
#     print("Add who you are, e.g. I am a first year student. ")

# print("===== Lab 5: Audience =====")
# audience = input("Audience (Who reads it): ")
# if len(audience) == 0:
#     print("No reader. AI uses a default adult style. ")
# elif "teacher" in audience or "classmate" in audience or "children" in audience:
#     print('Reader is clear')
# else:
#     print("Name the reader so AI picks the right words. ")

# print(" ===== Lab 6: Requirements =====")
# requirements = input("Requirements (what to include): ")
# if len(requirements) > 0 and ("and " in requirements or "," in requirements):
#     print("You listed more tham one point. Good")
# else:
#     print("List 2 or more points. Use 'and ' or a comma. ")

print("====== Lab 7: Constraints ======")
prompt = input("Your prompt: ")
length = len(prompt)
if length > 0:
    if length <= 200:
        print("Inside the limit.")
    else:
        print("Too long. Set a limit such as 'within 100 words'. ")
else:
    print("Empty prompt")

print()

# ---------- Nested if-else: score/absences (commented) + coffee/tea (active, from class18) ----------
# score = int(input("Score: "))
# absenses = int(input("Ansenses: "))
# if score >= 60:
#     print("Passed")
#     if score >= 90 and absenses <= 2:
#         print("With honors! ")
#     elif score >= 90:
#         print("high score, but too many absenses.")
#     else:
#         print("Good effort")
# else:
#     print("Failed")
#     if score >= 50:
#         print("Close! Try again")

drink = input("Coffee or Tea? ").upper()
size = input("size (S/M/L)? ").upper()

if drink == "COFFEE":
    if size == "L":
        price = 5
    elif size == "M":
        price = 4
    else:
        price = 3
elif drink == "TEA":
    if size == "L":
        price = 4
    elif size == "M":
        price = 3
    else:
        price = 2
else:
    print("We only have Coffee or tea")
    price = 0
print(f"Price: {price}")
