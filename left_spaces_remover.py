#Prog01: Create a program that ask the user to input their fullname with several space characters at 
# the beginning. Print the input without the spaces in the beginning.
#Example:
#Input:         Juan Dela Cruz
#Output: Juan Dela Cruz

#create a variable for a input 

ask_user = input('Please enter your name with several spaces in the beginning: ')

#use lstrip function

name = ask_user.lstrip()

#print the name

print(name)