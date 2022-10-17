# Author: PCL 10/11/22

#Asking the user to input their first and last name into the console
first_name = input("What is your first name?")
last_name = input("What is your last name?")

#combining the user's inputs into their full name and printing it
#The original instructions would have cause the names to be put together without a space, to solve this you can add a space between the two names when combined
full_name = first_name + " " + last_name
print(full_name)