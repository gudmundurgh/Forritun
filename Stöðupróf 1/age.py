age = int(input("Enter your age: "))

if 0 <= age <= 34:
    print("Young")
if 35 <= age <= 50:
    print("Mature")
if 51 <= age <= 69:
    print("Middle-aged")
if 70 <= age:
    print("Old")
if age < 0:
    print("Invalid age")