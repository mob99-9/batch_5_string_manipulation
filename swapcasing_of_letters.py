#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuaN deLA cRuz

#ask user for name 

name = str(input('Please enter your name with any incorrect casing :'))

#use swapcase function to fix capitalizations on the name

print(name.swapcase())