# age = int(input("Age: "))
# has_id = True

# if age >= 18 and has_id:
#     print("Can Enter")

# if age < 18 or not has_id:
#     print("Cannot enter")
    
# if age >= 13 and age <= 19:
#     print("Teen")
    
# if not age >= 13 and age <= 19:
#     print("Not teen")
    
    
# score = 50
# att = 90
# vip = True

# if score >= 60 and att >=75 or not vip:
#     print("Pass")
# else:
#     print("NO PASS")

print("=== SECURE LOGIN SYSTEM ===")

# Challenge 1: Login attempts
attempts = 0
login_success = False

while attempts < 3 and not login_success:

    # Input
    user = input("\nUsername: ")
    pw = input("Password: ")
    role = input("Role (admin/user): ")
    code = input("2FA code (or skip): ")

    # Challenge 3: Password strength checker
    if len(pw) >= 8 and "!" in pw:
        print("Strong password")
    else:
        print("Weak password")

    # Check admin login
    if user == "admin" and pw == "1235" and role == "admin":

        # Challenge 2: Time-based admin access
        hour = int(input("Enter hour (0-23): "))

        if hour >= 9 and hour <= 17:

            if code == "8888":
                print("Full admin access granted")
                print("Welcome to the admin panel")
                login_success = True

            elif code == "skip":
                print("Login OK (no 2FA)")
                login_success = True

            else:
                print("Incorrect 2FA code")
                attempts += 1

        else:
            print("Admin access is only allowed between 9:00 and 17:00")
            attempts += 1

    # Check guest login
    elif user == "guest" and pw == "guest" and role == "user":

        if code == "9999" or code == "skip":
            print("Guest access granted")
            login_success = True

        else:
            print("Incorrect 2FA code")
            attempts += 1

    # Incorrect login details
    else:
        print("Access denied")
        attempts += 1

    # Display remaining attempts
    if not login_success and attempts < 3:
        print("Attempts remaining:", 3 - attempts)


# Lock account after 3 failed attempts
if attempts >= 3:
    print("\nACCOUNT LOCKED!")
    print("Too many failed login attempts.")

print("\n=== SESSION ENDED ===")