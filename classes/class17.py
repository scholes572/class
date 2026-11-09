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
# if len (audience) == 0:
#     print("No reader. AI uses a default adult style. ")
# elif "teacher" in audience or "classmate" in audience or "children" in audience:
#     print('Reader is clear')
# else:
#     print("Name the reader so AI picks the right words. ")

# print(" ===== Lab 6: Requirements =====")
# requirements = input("Requirements (what to include): ")
# if len (requirements) > 0 and ("and " in requirements or "," in requirements):
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