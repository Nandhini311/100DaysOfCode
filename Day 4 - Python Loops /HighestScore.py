student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

'''sum'''
FindSum = 0
for value in student_scores:
    FindSum = FindSum + value

print(FindSum)
print(sum(student_scores))

'''max'''

maximum = 0
for value in student_scores:
    if maximum < value:
        maximum = value

print(maximum)
print(max(student_scores))

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

