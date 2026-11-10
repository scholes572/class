# ============================================================
# TOPIC: Print, Hello World, Strings & f-Strings
# Consolidated from: class2, class9, class10, class13, class15
# ============================================================

# ---------- Hello World / basic prints (from class2) ----------
print("Hello, python")
print("Welcome to the AI tools class")
print("Agostino Scholes Omare")

name = "Scholes"
print("Hello " + name + "!")
print(f"Nice to meet you {name}")

name = input("What is your name? ")
print(f"Your name is {name}")

country = input("Where do you come from? ")
print(f"{country} is a beautiful country")

print()

# ---------- String demos / privacy-safe prints (from class9) ----------
# item1 = "full ID number"
# item2 = "Personal Phone number"
# item3 = "Address"
# print(f"[FORBIDDEN] {item1}")
# print(f"[FORBIDDEN] {item2})

place1 = "Exact home address with your room number"
place2 = "real-time GPS Location"
# print(f"[FORBIDDEN] {place1}")
# print(f"[FORBIDDEN] {place2}")
print("city name length: ", len("Shenyang"))

safe = "Share only city or district level"
print("[SAFE]", safe)
print("city level confirmed", safe == "Shenyang")

print()

# ---------- String operations / f-strings (from class10) ----------
# greeting = "Hello"
# name = "Scholes"
# city = "Shenyang"
# print(greeting + name)
# print(greeting + " " + name)
# sentence = greeting + ", I am " + name + " from " + city + "."
# print(sentence)
# print(greeting, name, "from", city)

# line = "=" * 30
# print(line)
# print("My program ")
# print(line)

# stars = "*" * 3
# pattern = stars + " " + stars + " " + stars
# print(pattern)
# print("ha " * 3)

# s1 = "hello"
# s2 = "hello"
# s3 = "Hello"
# print("1:", s1 == s2)
# print("2:", s1 == s3)
# print("3:", s1 != s3)

# name = "Omare"
# age = 20
# print(name + " is " + str(age) + " years old.")

# num = 42
# num_text = str(num)
# print(num_text, type(num_text))

# price_text = "99"
# print(int(price_text))

print()

# ---------- f-string demos (from class15) ----------
# city = "Shenyang"
# print(f"I live in {city}")

# score = 95
# print(f"Your score is {score}/100")

# name = "Alice"
# age = 21
# color = "blue"
# print(f"Name: {name}")
# print(f"{name} is {age} years old")
# print(f"{color} is {name}'s faourite")

# name = input("Your name: ")
# food = input("Favourite food: ")
# num = int(input("Lucky number: "))
# print(f"Hello {name}")
# print(f"You like {food}")
# print(f"Your lucky number is {num}")
# print(f"{num} * 2 =  {num * 2}")

print()

# ---------- String concatenation / joining (from class13) ----------
# text = "I love "
# text += "Python "
# text += "programming."
# print(text)

# result = ""
# for i in range(1,5):
#     result += f"item{i} "
# print(result)

# words = ["Hello ","World ","Python"]
# result = "".join(words)
# print(result)
# csv = ",".join(words)
# print(csv)
# dashed = "- ".join(words)
# print(dashed)

# first = "Agostino"
# last = "Scholes"
# full = first + last
# print(full)
