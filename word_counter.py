#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
#Example:
#Input: We will weather the weather whatever the weather whether we like it or not
#Output: 14

#ask user for a sentence

ask_user = str(input('Please enter a complete sentence:  '))

#use split and len function and print the statement

sentence = ask_user.split()

print (len(sentence))