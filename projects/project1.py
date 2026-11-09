# I tried my best Laoshi :)
# student ID
student_id = input("Enter student's ID: ")

while len(student_id) != 8:
    print("ID must have 8 digits!")
    student_id = input("Enter student ID: ")

while not student_id.isdigit():
    print("ID must contain numbers only!")
    student_id = input("Enter student's ID: ")

# student name
name = input("Enter student name: ")

# student age
age = input("Enter student age: ")
while not age.isdigit() or int(age) < 15 or int(age) > 45:
    print("Age must be strictly between 15 and 45!")
    age = input("Enter student age: ")

# Student major
major = input("Enter student's major: ")

# Generated campus email
email = student_id + "@campussycu.com"

# Final student information
print("\n|======================================|")
print("|        STUDENT INFORMATION           |")
print("|======================================|")
print(f"Student ID   : {student_id}")
print(f"Name         : {name}")
print(f"Age          : {age}")
print(f"Major        : {major}")
print(f"Email address: {email}")
print("|======================================|")
