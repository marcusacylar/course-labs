# Create a dictionary named ProtocolsDict that will hold the following keys and values: {FTP: 21, DNS: 53, LDAP: 389, MySQL: 3306}
print("This program will display the port number of a given protocol.\n")

ProtocolsDict = {'FTP':'21', 'DNS':'53', 'LDAP':'389', 'MySQL':'3306'}
# Create a variable named question that will ask the user for the name of a service using the input() function.
question = input("For which protocol would you like to know the port number? ").upper()  # upper() converts lowercase to uppercase
# Create a condition to check if the value in the question variable exists in the dictionary.
# It should be checked against the dictionary’s key list.
if question in ProtocolsDict.keys():
    # Select a value from the dictionary with the question variable as a key
    answer = ProtocolsDict[question]
    # Print a message displaying the port associated with the selected service.
    print("The port number for protocol " + question + " is " + answer + "!")
# Finally, if the condition is not met, print a message that states that the protocol cannot be found.
else:
    print("The protocol can't be found")
