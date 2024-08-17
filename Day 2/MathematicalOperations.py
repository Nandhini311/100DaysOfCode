print("My age: " + str(12))
print(7-5)
print(7*2)
print(8/2) #dividing always gives a floating point number -> implicit typecasting
print(8//2) #no implicit type casting -> all the decimal points are removed.
print(8**2) #exponents; 8^2

#PEDMAS
## priority order -> (), **, / OR * , + OR -
print(3 * 3 + 3/3-3)


#change the output so it ouput is 3
print( 3 * (3+3)//3 - 3)


## BMI calculation 
bmi = 84 / 1.65 ** 2

#number manipulation.
print(bmi)

#flooring -> removing all the decimal places using int()
print(int(bmi))

#rounding a number to the nearest whole number
print(round(bmi, 2)) #inputs for round function, decimal number and the number of digits you want to round to

#number manipulaton
a = 0
a += 2
print(a)
a -= 1
print(a)
#you can do the same with * and /

