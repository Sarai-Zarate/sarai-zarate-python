name = "Sarai" 
age = 42
height = 5.6
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

name = input("What is your name? ")
birth_year = int(input("What is your birth year? "))
age = 2026 - birth_year

print(f"Hi, {name}! You are approximately {age} years old.")

weight = float(input("What is your weight? "))
height = float(input("What is your height? "))
print(f"{weight} x {height} = {weight * height:.1f}")

print()

item_name = "CTD Hoodie"
item_price = 59.99
quantity = 1
total = item_price * quantity

print('=====================')
print()
print('RECEIPT')
print()
print('=====================')
print()
print(f"Item: {item_name}")
print(f"PRICE: ${item_price:.2f}")
print(f"QUANTITY: {quantity}")
print()
print('=====================')
print(f"TOTAL: ${total:.2f}")

print()

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
hometown = input("What is your hometown? ")
favorite_hobby = input("What is your favorite hobby? ")
fun_fact = input("What is one fun fact about yourself? ")
birth_year = int(input("What is your birth year? "))

print("╔══════════════════════════════╗")
print()
print("PROFILE:", first_name + " " + last_name)
print()
print("╚══════════════════════════════╝")
print()
print(f"{'Hometown:':<12} {hometown}")
print(f"{'Hobby:':<12} {favorite_hobby}")
print(f"{'Fun Fact:':<12} {fun_fact}")
print(f"{'Age:':<12} {2026 - birth_year}")




