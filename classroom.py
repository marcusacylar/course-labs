# Create a for loop using the range function to iterate the loop 7 times
classroom = []
for i in range(7):
    # Each iteration should append a new empty list to the classroom list seven times
    # Each nested list will represent a separate classroom
    # Note: Doing this means you will be appending an empty list as an item of the classroom list
    classroom.append([])
    # print(classroom) # adding print statements here and there to see what's happening
    # Create a new for loop in the first loop that will iterate from 1 to 10
    for students in range(1, 11):
        # In the second loop, populate the nested lists with the iterated range 1-11
        classroom[i].append(students)
        #print(classroom)
# Outside the loops, print the end result of the populated list
print(classroom) # Prints 7 classrooms of 10 students
