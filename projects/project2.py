

###PROJECT 2#####
number = int(input("Please enter the number of Students: "))
while number <= 0:
    print("Please enter a number greater than 0!")
    number = int(input("Please re-enter the number of students: "))
print(f"The number of students: {number}")

students = []
for i in range(number):
    print("\nstudent" , i + 1)
    name = input("Enter the student's name: ")
    
    scoreI = float(input("Enter the 1st score: "))
    while scoreI < 0 or scoreI > 100:
        print("Invalid Score!")
        scoreI = float(input("Re-enter the 1st score: "))

    scoreII = float(input("Enter the 2nd score: "))
    while scoreII < 0 or scoreII > 100:
        print("Invalid Score!")
        scoreII = float(input("Re-enter the 2nd score: "))

    scoreIII = float(input("Enter the 3rd Score: "))
    while scoreIII < 0 or scoreIII > 100:
        print("Invalid score!")
        scoreIII = float(input("Re-enter the 3rd score: "))
    
total = scoreI + scoreII + scoreIII
average = total/3
            

if average >=80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"
print("Grade:", grade)

students.append([name, total, average, grade])

print("\n Students Results: ")

for student in students:
    print(student)

for i in range (len(students)):
    for j in range(i + 1, len(students)):
        if students[i] [2] < students [j] [2]:
            students [i], students [j] = students[j]
students[i]

print("\n===============RANKED STUDENT RESULTS ==================")
print("Rank | Name | Total | Average | Grade")

for i in range(len(students)):
    print(
        i + 1, "|",
        students[i][0], "|",
        students[i][i], "|",
        round(students[i][2], 2), "|",
        students[i][3]
    )
class_total = 0
for student in students:
    class_total = class_total + student[2]
class_average = class_total / number 

highest_total = students[0] [1]
for student in students:
    if student[1] > highest_total:
        highest_total = student[1]
        
print("\n =========== THE STATISTICS===============")
print("Number of students:", number)
print("Class average:", round(class_average, 2))
print("Highest student total: ", highest_total)
print("Top student: ", students[0][0])