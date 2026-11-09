# item1 = "full ID number"
# item2 = "Personal Phone number"
# item3 = "Address"
# item4 = "Personal businness number"
# item5 = "Other personal number"
# item6 = "Email address"
# print(f"[FORBIDDEN] {item1}")
# print(f"[FORBIDDEN] {item2}")
# print("Description length:" ,len(item1))
# print("Description length:" ,len(item2))
# print("Description length:" ,len(item3))
# print("Description length:" ,len(item4))
# print("Description length:" ,len(item5))
# print("Description length:" ,len(item6))

# print(f"[FORBIDDEN] {item3}")
# print(f"[FORBIDDEN] {item4}")
# print(f"[FORBIDDEN] {item5}")
# contains_private = True
# print("Contains private info:", contains_private)

# safe_1 = "A contact method, no digits"
# safe_2 = "A contact method, no digits"
# print(f"[SAFE] {safe_1}")
# print("Demo number length:", len("00000000000"))
# safe_1 == safe_2

# sec1 = "Account login password"
# sec2 = "SMS code"
# payment_pin = "Payment pin"

# print("[FORBIDDEN]", sec1)
# print("[FORBIDDEN]", sec2)
# print(f"[FORBIDDEN] {payment_pin}")
# print("Kept private:", len(sec1) > 0)

# password_shared = False
# print(f"Shared with a tool: {password_shared}")
# safe = "Complete login on the official page"
# print(f"[SAFE] {safe}")
# print(f"Safe action confirmed {safe}" == "compelete login on the official page")

# name = "Alice"
# city = 'Shenyang'
# email = "alice@uni.edu"
# print(name)
# print(city)
# print(type(email))
# nothing = ""
# print(nothing)

# age_num = 20
# age_str = "20"
# print(age_num + 5)
# print(age_str + "5")

# msg = "It's a cat"
# msg2 = 'He said "hi"'
# print(msg)
# print(msg2)


# name = "Alice"
# print(len(name))
# city = "Shenyang"
# print(len(city))


# first_name = "Agostino"
# last_name = "Scholes"
# country = "Kenya"
# hobby = "Playing games"

# print(first_name)
# print(last_name)
# print(country)
# print(hobby)
# print(type(first_name), len(first_name))
# print(type(country), len(country))
# third_name = ""
# print(len(third_name))


# print('''I'm Learning python''') 
# print('He said "Hello"')
# bad  = "Alice"
# The error I see is the variable is not called


# first = "Hello"
# second = "World"
# both = first + second

# print(both)
# both = first + " " + second
# print(both)


place1 = "Exact home address with your room number"
place2 = "real-time GPS Location"
print(f"[FORBIDDEN] {place1}")
print(f"[FORBIDDEN] {place2}")
print("city name length: ", len("Shenyang"))

exact_location_used = False
print(f"Exact location used: {exact_location_used}" )
print("-" * 30)
safe = "Share only city or district level"
print("[SAFE]", safe)
print("city level confirmed", safe == "Shenyang")

content1 = "Personal dairy entries"
content2 = "Private photos and videos"
print("[FORBIDDEN]", )

claim1 = "an unverified sensational rumor"
print("[CHECK]", claim1)
print("Needs verification")
is_verified = False
print(f"information verified {is_verified}")
official_source = "Official verified channel"