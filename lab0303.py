# Create a variable to be used as a counter and set its value to zero, since it will be the counter's starting point.
counter = 0
# Create a while loop with a condition that checks if the counter's value is less than 10.
while counter < 10:
    # In the loop, add +1 to the counter with each iteration
    counter += 1
    print(counter) # added to see the iteration
    # Create an if statement that checks if the counter equals 6
    if counter == 6:
        # If the counter equals 6, print "Found!" and exit the while loop
        print("Found!")
        break