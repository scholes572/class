name = input("What is your name? ")
print(f"Hello, {name}")
age = input("Age: ")
print(type(age))

name = input("Name: ")
city = input("City: ")
hobby = input("Hobby: ")

print("--- Your Info ---")
print(f"Name: {name}")
print(f"City: {city}")
print(f"Hobby: {hobby}")

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

