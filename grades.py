# Request the user to input a grade and assign it to a variable named grade
# Convert the variable to an integer
grade = int(input("Enter a grade: "))

# Create a condition that checks if the grade is equal to or higher than 90, and if so print A
if grade >= 90:
    print("A")
# Create a condition that checks if the grade is equal to or higher than 80, and if so print B
elif grade >= 80:
    print("B")
# Create a condition that checks if the grade is equal to or higher than 80, and if so print B
elif grade >= 70:
    print("C")
# Create a condition that checks if the grade is equal to or higher than 80, and if so print B
elif grade >= 65:
    print("D")
# Create a condition that checks if the grade is equal to or higher than 80, and if so print B
elif grade >= 0:
    print("F")
# Finally, the code should print an error message if the user inserted an invalid number, such as a negative number
else:
    print("ERROR: Grades cannot be negative numbers or words")
