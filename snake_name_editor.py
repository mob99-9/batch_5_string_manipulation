#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
#Example:
#Input: jUAn DEla CrUZ
#Output: juan_dela_cruz

#ask user for name 

name = str(input('Please enter your name: '))

#use lower function to lower all letter on the name

name = name.lower()

#use replace function to replace spaces to "_" and print the name

print(name.replace(" ", "_"))