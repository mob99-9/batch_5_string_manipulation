#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuanDelaCruz

#ask user for name 

name = str(input('Please enter your name: '))

#use title function to capitalize properly the name

name = name.title()

#use replace function to remove space and print the name

print(name.replace(" ", ""))