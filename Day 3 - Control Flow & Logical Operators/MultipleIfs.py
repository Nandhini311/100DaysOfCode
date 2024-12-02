print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Please enter your age"))
    if age < 12:
        bill=5
        print(" You have to pay 5$")
    elif age<=18 :
        bill=6
        print("You have to pay 6$")
    else:
        bill=7
        print("You have to pay 7$")

    want_photo = input("Do you want to have your photo taken? Type y for Yes and n for No")
    if want_photo == 'y':
        bill += 3
    print(f"Here is your bill {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

