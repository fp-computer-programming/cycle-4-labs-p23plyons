# Author: PCL 10/18/22

#creating the input vairable for the 6 letter DNA sequence's
#creating a variable for the new complementary DNA sequence to be put into
dna = input("Please input your 6 letter DNA sequence")
complementary = ""

#creating a new string with the complementary DNA sequence by checking each index of the inputed string
#and placing the complementary letter into a new string
if dna[0] == "a":
    complementary += "t"
elif dna[0] == "t":
    complementary += "a"
elif dna[0] == "c":
    complementary += "g"
elif dna[0] == "g":
    complementary += "c"

if dna[1] == "a":
    complementary += "t"
elif dna[1] == "t":
    complementary += "a"
elif dna[1] == "c":
    complementary += "g"
elif dna[1] == "g":
    complementary += "c"

if dna[2] == "a":
    complementary += "t"
elif dna[2] == "t":
    complementary += "a"
elif dna[2] == "c":
    complementary += "g"
elif dna[2] == "g":
    complementary += "c"


if dna[3] == "a":
    complementary += "t"
elif dna[3] == "t":
    complementary += "a"
elif dna[3] == "c":
    complementary += "g"
elif dna[3] == "g":
    complementary += "c"

if dna[4] == "a":
    complementary += "t"
elif dna[4] == "t":
    complementary += "a"
elif dna[4] == "c":
    complementary += "g"
elif dna[4] == "g":
    complementary += "c"

if dna[5] == "a":
    complementary += "t"
elif dna[5] == "t":
    complementary += "a"
elif dna[5] == "c":
    complementary += "g"
elif dna[5] == "g":
    complementary += "c"

#Printing the complementary DNA sequence string
print(complementary)