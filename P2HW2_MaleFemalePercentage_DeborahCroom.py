
#Write a program that asks for the # of males and females in a class and display the percentage
#10/24/18
#CTI-110 P2HW2 - Male Female Percentage
#Deborah Croom

#Suppose there are 8 males and 12 females in a class
#There are 20 students in a class
#Percentage of males is calculated as 8/20=40%
#Percentage of females calculated as 12/20=60%

males = int(input("Enter the number of males in the class:"))
females = int(input("Enter the number of females in the class:"))
totalStudents = males + females

malePercentage = (males/totalStudents) * 100
femalePercentage = (females/totalStudents) * 100

print("Male percentage: " + str(malePercentage))
print("Female percentage: " + str(femalePercentage))

