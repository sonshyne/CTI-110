Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> #Write a program that asks for the # of males and females in a class and display the percentage
>>> #10/17/18
>>> #CTI-110 P2HW2 - Male Female Percentage
>>> #Deborah Croom
>>> 
>>> #Suppose there are 8 males and 12 females in a class
>>> #There are 20 students in a class
>>> #Percentage of males calculated as 8/20=40%
>>> #Percentage of females calculated as 12/20=60%
>>> 
>>> males=int(input("Enter the number of males in the class:"))
Enter the number of males in the class:8
>>> females=int(input("Enter the number of females in the class:"))
Enter the number of females in the class:12
>>> totalStudents=males+females
>>> malePercentage=(males/totalStudents)*100
>>> femalePercentage=(females/totalStudents)*100
>>> print("Male percentage:"+str(malePercentage))
Male percentage:40.0
>>> print("Female percentage:"+str(femalePercentage))
Female percentage:60.0
>>> 
