# print("=== Grade Checker ===")
# name = input("Name: ")
# score = int(input("Score: "))
# attendance = int(input("Attendance %: "))
# if score >= 90:
#     print("Excellent!")
# if score > 60 and attendance>= 75:
#     print(f"{name}, you PASSED!")
#     print(f"Your score: {score}/100")
#     print("Good Job!") 
# elif score >= 60:
#     print(f"{name}, you PASSED the score requirement but your attendance is low!")
#     print(f"Your score :{score}/100")
#     print(f"Good job")
# else :
#     print(f"{name}, You FAILED")
#     print(f"Your score: {score}/100")
#     print("keep practising!")



print("=== Grade Calculator ===")
name = input("What is your name: ")
score = int(input("Insert score between (0-100)"))
score2 = int(input("Insert score 2 between (0-100)"))
score3 = int(input("Insert score 3 between (0-100)"))
average = (score + score2 +score3) /3


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
    if average>= 65:
        grade = "D"
        msg = "You getting there"
else:
    grade = "E"
    msg = "Keep studying!"


print(f"{name}: {grade} - {msg}")
print("=== Done ===")    