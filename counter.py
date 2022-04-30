# Create a variable that gets a number from the user to be used as the range function's upper limit
# Convert the input to an integer
upper_bound = int(input("Choose the range upper bound -->"))
# Create a for loop with the range function, where its starting point is 1, and its upper limit is
# the input from the user in the previous step
for x in range(1, upper_bound, 2):  # Print function will iterate by 2
    # Add a print function in the for loop that prints the result of each function
    print("The next number in line is {}".format(x))
