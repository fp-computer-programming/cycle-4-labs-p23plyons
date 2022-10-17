# Author: PCL 10/14/22

#creating needed strings
word = "flibbertigibbet"

#finding the index of the first letter t and printing the result
first_t = word.find("t")
print(first_t)

#finding the letter right after the first t and printing it
print(word[first_t+1])

#creating first_name string
first_name = "preston"

#printing fully uppercased first name
print(first_name.upper())

#creating last needed string
wish_string = "I wish, I wish, I was a fish"

#spliting the string at each comma and printing the result
print(wish_string.split(","))