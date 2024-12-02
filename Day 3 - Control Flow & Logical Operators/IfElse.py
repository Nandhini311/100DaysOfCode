print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if(height>120):
    print("Hooray ! you can ride the rollercoaster")
else:
    print("Sorry ! you cannot ride the rollercoaster")

#modulus operator -> gives the reminder
a = 10 % 3
print(a)

number = int(input("Enter the number you want to check"))
if (number % 2)==0:
    print("The number you entered is an even number")
else:
    print("The number you entered is an odd number")
