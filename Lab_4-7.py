# Author: PCL 10/18/22

#having the user input 5 random numbers
num1 = input("Please input your first random number")
num2 = input("Please input your second random number")
num3 = input("Please input your third random number")
num4 = input("Please input your fourth random number")
num5 = input("Please input your fifth random number")

#changing all of the numbers provided from strings to integers and printing them in a single line with a space between each
int(num1); int(num2); int(num3); int(num4); int(num5)
print (num1+" "+num2+" "+num3+" "+num4+" "+num5)

#finding the highest number of the numbers provided an printing the result
largestnum = max(num1,num2,num3,num4,num5)
print("Largest number given was "+largestnum)

#finding the lowest number of the numbers provided an printing the result
smallestnum = min(num1,num2,num3,num4,num5)
print("Smallest number given was "+smallestnum)