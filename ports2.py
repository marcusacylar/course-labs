# Create an infinite while loop
servicePorts = {}
while True:
    # Create a variable that asks for a service name
    service = input("Please enter a service's name or type '0' to stop: ").upper()
    # Add an if condition in the while loop to break the loop if the input from the user is 0.
    if service == "0":
        break
    # In the while loop, ask for a port number and assign it to the port variable
    port = input("Please enter a port number or type '0' to stop: ")
    # Add another if condition in the while loop to break the loop if the input from the user is 0
    if port == "0":
        break
    # Insert the data from the service and port variables as key-value pairs, in the empty dictionary
    # created during step 1.
    servicePorts[service] = port
# When the user decides to quit by pressing 0, print the entire dictionary
print(servicePorts)
