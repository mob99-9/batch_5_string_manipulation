#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: Juan Dela Cruz

#ask user for name 

name = str(input('Please enter your name with any incorrect casing :'))

#use title function to fix capitalizations on the name

print(name.title())