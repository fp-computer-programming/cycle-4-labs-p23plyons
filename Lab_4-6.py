# Author: PCL 10/18/22

# having the user input both their dish and their beast
dish = input("What dish will be brought out?")
beast = input("What animal will be bringing the dish?")

#checking if the first letter of the beast's name is the same as the first and last letter of the dish's name,
#and printing if they are allowed to bring their dish
if beast[0] == dish[0] and beast[0] == dish[len(dish)-1]:
    print ("The beast is allowed to bring the dish to the feast!")
else:
    print ("The beast is NOT allowed to bring the dish to the feast!")