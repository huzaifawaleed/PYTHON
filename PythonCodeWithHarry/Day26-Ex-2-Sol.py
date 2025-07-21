# Exercise 2 Solution

import time
t = time.strftime('%H:%M:%S') 
hour = time.localtime().tm_hour
# hour = int(input("Enter hour: "))
# print(hour)

if(hour>=5 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<21):
  print("Good Night Sir!")