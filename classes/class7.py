# BMI Calculator
weight = int(input("Weight of person : "))
height = int(input("Height of person : "))
BMI = weight / (height * height)
print(f"The current BMI of person is : {BMI}")

# Temperature calculator # jljb
fahrenheit = int(input("What's the current temp? "))
celsius = (fahrenheit - 32) * 5/9
print(f"The current temp is : {celsius}")

# Weekly pay hours
hours = int(input("Time of hours worked : "))
rate = float(input("Current rate : "))
weekly_pay = hours * rate
print(f"Salary of peson is : {weekly_pay}")

# Discount giver
price = int(input("Price of item: "))
discount_rate = int(input("Dicount rate : "))
Discount = price * (1 - discount_rate)
print(f"The discount is : {Discount}")