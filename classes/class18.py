# score = int(input("Score: "))
# absenses = int(input("Ansenses: "))

# if score >= 60:
#     print("Passed")
#     if score >= 90 and absenses <= 2:
#         print("With honors! ")
#     elif score >= 90:
#         print("high score, but too many absenses.")
#     else:
#         print("Good effort")
# else:
#     print("Failed")
#     if score >= 50:
#         print("Close! Try again")


drink = input("Coffee or Tea? ").upper()
size = input("size (S/M/L)? ").upper()

if drink == "COFFEE" : # .upper()
    if size == "L":
        price = 5
    elif size == "M":
        price = 4 
    else:
        price = 3
elif drink == "TEA":
    if size == "L":
        price = 4 
    elif size == "M":
        price = 3
    else:
        price = 2
else:
    print("We only have Coffee or tea")
    price = 0
print(f"Price: {price}")