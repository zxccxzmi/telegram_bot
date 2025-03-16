name = input("Enter your name! ")
last_name = input("Enter your last name! ")

name = name.capitalize()
print(name)
last_name = last_name.capitalize()
print(last_name)


name = (input("Enter your name: "))
age = (input("Enter your age: "))

if name.isalpha() and age.isdigit() and 0 < int(age) < 200:
    print(f"{name}, you are was born in {2025 - int(age)}")
else:
    print("Invalid data")
