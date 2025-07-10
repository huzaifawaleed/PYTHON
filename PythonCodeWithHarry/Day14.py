# Check if a number is positive, negative, or zero.

# num = int(input("Enter a number to check positive, negative, or zero: "))

# if(num == 0):
#     print("Number is ZERO")
# elif(num > 0):
#     print("Number is POSITIVE")
# elif(num < 0):
#     print("Number is NEGATIVE")
# else:
#     print("NOT a Number/Invalid")        



# Check if a number is even or odd.

# n = int(input("Enter a number to check positive, negative, or zero: "))

# if(n % 2 == 0):
#     print("Number is EVEN")
# else:
#     print("Number is ODD")




# Check if a year is a leap year.

# year = int(input("Enter Year To Check Leap Year or Not a Leap Year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("This is a LEAP YEAR")
# else:
#     print("Not a LEAP YEAR")




# Check if a number is divisible by 5 and 11.


# number = int(input("Enter a number to check it is divisible by 5 and 11: "))

# if(number % 5 == 0):
#     print("The Number is Divisible By 5")
# elif(number % 11 == 0):
#     print("The Number is Divisible By 11")    
# else:
#       print("The Number is NOT Divisible By 5 and 11")




# Check whether a character is an alphabet, digit, or special symbol.

# char = input("Enter anything to check alphabet, digit, or special symbol: ")

# if char.isalpha():
#     print("This is a ALPHABET")
# elif char.isdigit():
#     print("This is a DIGIT")
# elif char.isalnum():
#     print("This is a DIGIT & ALPHABETS")
# else:
#     print("This is a CHARACTER")        



# Check if a triangle is equilateral, isosceles, or scalene.

# a = "Enter Three Sides Of Triangle To Check Equilateral, Isosceles, or Scalene"
# print(a.center(100))
# s1 = int(input("Enter Side 1: "))
# s2 = int(input("Enter Side 2: "))
# s3 = int(input("Enter Side 3: "))

# if s1 == s2 == s3:
#     print("This is Equilateral Triangle")
# elif s1 == s2 or s2 == s3 or s1 == s3:
#     print("This is Isosceles Triangle")
# elif s1 != s2 and s2 != s3 and s1 != s3:
#     print("This is Scalene Triangle")
# else:
#     print("Invalid Sides")    






# Electricity bill calculator (based on units consumed).


# units = int(input("Enter Number Of Units To Calculate the Bill: "))

# cost1 = 5
# cost2 = 7
# cost3 = 10
# cost4 = 15
# totalBill = 0


# if units <= 100:
#     totalBill = cost1 * units
#     print("Total Units is =",units, "\nPer Unit cost is =",cost1,"  \nThe Total Bill is = ",totalBill)
# elif units == 101 or units <= 200: 
#      totalBill = cost2 * units
#      print("Total Units is =",units, "\nPer Unit cost is =",cost2,"  \nThe Total Bill is = ",totalBill)     
# elif units == 201 or units <= 300: 
#      totalBill = cost3 * units
#      print("Total Units is =",units, "\nPer Unit cost is =",cost3," \nThe Total Bill is = ",totalBill)
# elif units > 300: 
#      totalBill = cost4 * units
#      print("Total Units is =",units, "\nPer Unit cost is =",cost4," \nThe Total Bill is = ",totalBill) 
# else:
#      print("Please Enter Units?")





# Temperature status (cold, normal, hot).

# temp = float(input("Enter the Temperature to Check Status COLD, NORMAL, HOT: "))

# if temp <= 20.0:
#      print("The Temperture is COLD = ", temp)
# elif temp >= 21.0 and temp <= 35.0:
#      print("The Temperture is NORMAL = ", temp)     
# else:
#      print("The Temperture is HOT = ", temp)

# Check login credentials (simulate username and password check)

orgName = "Huzaifa"
orgPass = "123"
uName = input("Enter UserName: ")
uName.islower()
uPass = input("Enter UserPassword: ")
if uName == orgName and uPass == orgPass:
     print("Login")
else:
     print("Wrong Credentials!")     



# Find the day of the week based on number (1 = Monday, ..., 7 = Sunday)