# ============================================================
# TOPIC: Loops - for / while
# Consolidated from: class8, class19
# ============================================================

# ---------- for loop with if inside (from class8) ----------
for number in range(1, 8):
    if number > 4:
        print(number)

print()

# ---------- for / while loop demos (commented, from class19) ----------
# for o in range(10):
#     print("Hi ")

# for i in range(5):
#     print(f"Round {i}")

# for i in range(3):
#     print(f"{i} squared = {i * i}")

# for i in range(7):
#     print("Hi")

# for n in range(10):
#     print(f"{n}")

# for i in range(4):
#     print(f"{i} * 2 = {i * 2}")

# for x in range(3):
#     print(f"round {x}")

# for i in range(1):
#     print("A")
#     print("B")
# print("C")

# for i in range(4):
#     if i > 1:
#         print(i)

# for count in range(3):  # This shows that any name works...not only i. I is the traditional!!!
#     print(count)

# for number in range(5):
#     print(f"Num: {number}")

# for i in range(3):
#     print(f"Start {i}")
#     print(f"End {i}")

# for i in range(3):
#     print("Inside")
# print("Outside")

# count = 0
# while count < 5:
#     print(count)
#     count = count + 1.5

# total = 1
# for i in range(1, 6):
#     total = total + i
# print(total)

# for i in range(7):
#     print("Hi")

# for n in range(0, 10):
#     print(n)

# for number in range(3):
#     print(f"Round {number}")

# for i in range(3):
#     print("A")  # A prints 3 times
#     print("B")  # B prints 3 times
# print("C")  # C prints 1 time!

# for i in range(4):
#     if i > 1:
#         print(i)  # This prints 2 and 3 only

# for i in range(2, 7):
#     print(i)
# for i in range(0, 10, 3):
#     print(i)

# for i in range(1, 6):
#     print(i)

# for number in range(10, 0, -2):
#     print(number)

# for i in range(0, 3):
#     print(i / 2)

# for a in range(1, 6):
#     print(a)
# for b in range(9):
#     print(b)
# for c in range(10, 5, -1):
#     print(c)
# for d in range(3, 13, 3):
#     print(d)
# for e in range(100, 60, -10):
#     print(e)
# for f in range(5, -1, -1):
#     print(f)

# total = 0
# for i in range(1, 6):
#     total = total + i
# print(f"Sum  = {total}")

# count = 0
# for i in range(1, 11):
#     if i % 2 == 0:
#         count = count + 1
# print(f"Even numbers: {count}")

# product = 1
# for i in range(1, 4):
#     product = product * i
# print(f"3! = {product}")

# total = 0
# for i in range(1, 11):
#     total = total + i
# print(total)

# count = 0
# for n in range(1, 21):
#     if n % 3 == 0:
#         count = count + 1
# print(count)

# result = 1
# for i in range(1, 6):
#     result = result * i
# print(result)

# total = 0
# for i in range(1, 5):
#     total = total + i * 2
# print(total)

# total = 0
# for i in range(1, 5):
#     total = total + (i * 2)
# print(total)

# total = 0
# count = 5
# for i in range(count):
#     num = float(input(f"Number {i + 1}: "))
#     total = total + num
# average = total / count
# print(f"Average = {average}")

# n = int(input("n = "))
# total = 0
# for i in range(1, n + 1):
#     square = i * i
#     total = total + square
#     print(f"{i} ^ 2 = {square}")
# print(f"Sum of squares = {total}")

print()

# ---------- Active: grade calculator with for loop (from class19) ----------
print("=== Grade Calculator ===")
n = int(input("How many scores? "))
total = 0
highest = 0
lowest = 100
passed = 0

for i in range(n):
    score = float(input(f"Score {i + 1}: "))
    total = total + score
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
    if score >= 60:
        passed = passed + 1

avg = total / n
print(f"Total: {total}")
print(f"Average: {avg:.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
