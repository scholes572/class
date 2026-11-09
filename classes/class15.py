# name = "Tom"
# age = 20
# print("Name:", name, "Age:", age)
# print(f"Name: {name}, Age: {age}")

# city = "Shenyang"
# print(f"I live in {city}")

# score = 95
# print(f"Your score is {score}/100")

# print("Name", name, "Age:", age, "City:", city)
# print(f"{name} ({age}) from {city}: {score}")

# name = "Alice"
# age = 21
# color = "blue"
# print(f"Name: {name}")
# print(f"{name} is {age} years old")
# print(f"{color} is {name}'s faourite")
# print(f"Hello, {name}!. You are {age} years old")

# name = input("Your name: ")
# food = input("Favourite food: ")
# num = int(input("Lucky number: "))
# print(f"Hello {name}")
# print(f"You like {food}")
# print(f"Your lucky number is {num}")
# print(f"{num} * 2 =  {num * 2}")
# # Q1 = If i forget if, the code will not work
# # Q2 = No we can't use {} without f

print("=== Shop Receipt ===")
item = input("Item name: ")
price1 = float(input("What is the price? "))
item2 = input("Item 2 name")
price2 = float(input("What is the price: "))
qty = int(input("Quantity: "))
rate = 1.08

total = price2 + price1 + qty
print(f"The following is the receipt {total}")

print("--------------------")
print(f"item: {item}")
print(f"Price: {price}")
print(f"Quantity: {qty}")
print(f"Total: {total * rate}")
print(f"The total")
print("=====================")
