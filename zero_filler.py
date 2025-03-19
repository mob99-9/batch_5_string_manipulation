#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit 
# format. Add zeros at the beginning to complete the 6 digit.
#Example:
#Input: 143
#Output: 000143

#ask user for a number from 0 to 1000

ask_user = input('Please enter a number from 0 to 1000: ')

#use zfill function 

number = ask_user.zfill(6)

#display the number

print(number)