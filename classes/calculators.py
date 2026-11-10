# ============================================================
# TOPIC: Calculators (BMI, Temperature, Pay, Discount, Receipt)
# Consolidated from: class7, class15
# ============================================================

# ---------- BMI Calculator (from class7) ----------
weight = int(input("Weight of person : "))
height = int(input("Height of person : "))
BMI = weight / (height * height)
print(f"The current BMI of person is : {BMI}")

# ---------- Temperature calculator (from class7) ----------
fahrenheit = int(input("What's the current temp? "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"The current temp is : {celsius}")

# ---------- Weekly pay hours (from class7) ----------
hours = int(input("Time of hours worked : "))
rate = float(input("Current rate : "))
weekly_pay = hours * rate
print(f"Salary of peson is : {weekly_pay}")

# ---------- Discount giver (from class7) ----------
price = int(input("Price of item: "))
discount_rate = int(input("Dicount rate : "))
Discount = price * (1 - discount_rate)
print(f"The discount is : {Discount}")

print()

# ---------- Shop receipt (active, from class15) ----------
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
print(f"Price: {price1}")
print(f"Quantity: {qty}")
print(f"Total: {total * rate}")
print("=====================")
