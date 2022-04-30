# Create a variable named input_ip and assign it user input
input_ip = input("Please enter an IPv4 address: ")
# Extract octets from the input_ip variable created in the previous task using split() and specifying "." as a delimiter. Save the result to a new variable named ip_segments
ip_segments = input_ip.split(".")
# Use an if statement to verify the number of octets in ip_segments from the previous task, using len(). If it's different than 4 octets, print "illegal IPv4 address" to the console, and use quit() to terminate execution
if len(ip_segments) != 4:
    print("Illegal IPv4 address.")
    quit()
# Following the if block from previous task, create a variable named ip_as_binary and assign it an empty list
ip_as_binary = []
# Create a for loop using a variable named octet that will iterate through the previously created list ip_segments
for octet in ip_segments:
    num = int(octet)
    bin_num = bin(num)[2:]
    while len(bin_num) < 8:
        bin_num = "0" + bin_num
    ip_as_binary.append(bin_num)
# Within the for loop scope, use slice notations to exclude the "0b" prefix value from bin_num, and append the result to the ip_as_binary list
# ip_as_binary.append(bin_num[2:])
# A binary octet consists of 8 bits. Improve the code from previous tasks to print the result octets with the additional 0s needed (e.g. "1.1.1.1" should output "00000001.00000001.00000001.00000001")
# bin_num = bin(num)[2:]

# Following the for loop from previous task, write a one-liner that uses join() to add all octets within ip_as_binary into a single string, separated by a dot ("."), and print the results
print(".".join(ip_as_binary))
