print("Hello"[0]) #should get the first letter.
print("Hello"[-1]) #Should get the last letter, -2 for second last letter

#string - anything under "" quotation
name = "Nandhini"
print(name)

#integer - whole numbers
print(123+456)
a = 1 #no need to mention specifically int

#big numbers -> the underscores (used instead of commas) are automatically removed in python
b = 123_456_8910
print(b)

#float -> Decimal numbers
c = 89.78

#boolean
d = True

#type gives the data type details. 
print(type(a))
print(type(name))
print(type(c))
print(type(d))

#data type conversion
print(int("123")+int("456")) #though 123 is under quotation, int function helps in converting it into an integer.
print(float(123))
print(str(123))
print(bool("True"))

#correct this line of code - print("Number of letters in your name: " + len(input("Enter your name")))
#answer: string cannot be concatenated with an integer
print("Number of letters in your name: " + str(len(input("Enter your name"))))
